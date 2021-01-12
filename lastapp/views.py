from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from lastapp.serializer import BookModelSerializer
from modapp.models import Book
from utils.response import APIResponse


class BookGenericAPIView(GenericAPIView,ListModelMixin,
                         RetrieveModelMixin,
                         CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        if "id" in kwargs:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        response = self.create(request,*args,**kwargs)
        return APIResponse(results=response.data)

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(results=response.data)