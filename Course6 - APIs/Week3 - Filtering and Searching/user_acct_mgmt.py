# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import isAdminUser
from django.contrib.auth.models import User, Group

@api_view(['POST'])
@permission_classes([isAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        # managers.user_set.add(user)
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({'message': 'ok'})

    return Response({'message': 'Eroor'}, status.HTTP_400_BAD_REQUEST)

# urls.py
path('groups/manager/users', views.managers)