from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer
from rest_framework import status

class BookViewSet(APIView):
    def get(self):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer, status= status.HTTP_200_OK)

