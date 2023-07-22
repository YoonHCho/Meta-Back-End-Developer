from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def books(request):
    return Response('List of the Books', status=status.HTTP_200_OK)


'''
Function and Class based views
'''
# views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if (author):
            return Response({"message": "list of the books by " + author}, status.HTTP_200_OK)

        return Response({"message": "List of the books"}, status.HTTP_200_OK)

    def post(self, request):
        return Response({"title": request.data.get('title')}, status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, request, pk=None):
        return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk=None):
        return Response({"title": request.data.get('title')}, status.HTTP_200_OK)

# urls.py
from django.urls import path
from . import views
urlpatterns = [
    # path('books/', views.books),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view()),
]
