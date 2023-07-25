from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage

@api_view(['GET', 'POST'])
def menu_item(request):
    # return Response('List of books', status=status.HTTP_200_OK)
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        # to implement filtering
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        if category_name:
            items = items.filter(category__title=category_name) # category is the model __ and title is the field: This title field belongs to the category model and is linked to the menu item model.
        if to_price:
            items = items.filter(category__lte=to_price) # lte is a conditional operator or fields lookup and the price double underscore lte means price is less than or equal to a value

        # to implement search
        search = request.query_params.get('search')
        if search:
            items = items.filter(title__icontains=search) # the prefix i in icontains will search and filter values case insensitive.

        # to implement ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            # when ordering by a single column
            # items = items.order_by(ordering) # order by a field, this case, price/title/category etc. by default-ascending, to sort by descending order add a minus sign - as prefix inside the parenthesis.
            # when ordering by more than one column
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields) # * is used for argument unpacking. by using * before ordering_fields, the list elements are unpacked, and each field in the list becomes a separate argument to the order_by() method.

        # to implement pagination
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST': # to deserialize data
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        # serialized_item.validated_data # if you need to access data before calling the save method, you can use this
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view()
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)