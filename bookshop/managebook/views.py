from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from managebook.models import Book
from managebook.serialize import BookSerializer


class ListBook(ListAPIView):
    serializer_class = BookSerializer

    # def get_queryset(self, request, id=None):
    #     if id is None:
    #         return Response(BookSerializer(Book.objects.all()))
    #     return Response(BookSerializer(Book.objects.all(id=id)).data)
    def get_queryset(self):
        if self.kwargs.get('id'):
            return Book.objects.filter(id=self.kwargs.get('id'))
        return Book.objects.all()


class CreateBook(CreateAPIView):
    serializer_class = BookSerializer

class DestroyBook(DestroyAPIView):
    # def get_object(self):
    #     return Book.objects.get(id=self.kwargs['id'])

    lookup_field = 'id'

    def get_object(self):
        return Book.objects.all()