from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from modapp.models import Book
from modapp.serializer import BookModelSerializer, BookDeModelSerializer


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book_id = request.GET.get('id')
        print(book_id,111)
        if book_id:
            book_obj = Book.objects.filter(pk=book_id).first()
            data = BookModelSerializer(book_obj).data
            return Response({"message": "查询单个成功", "results": data})
        else:
            query_set = Book.objects.all()
            data = BookModelSerializer(query_set, many=True).data
            return Response({"message": "查询成功", "results": data})

    def post(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)
        if isinstance(request_data, dict) and request_data != {}:
            many = False
        elif isinstance(request_data, list) and request_data != []:
            many = True
        else:
            return Response({
                'message': '参数有误'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookDeModelSerializer(data=request_data, many=many)
        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()
        return Response({
            'message': '新增图书成功',
            'result': BookModelSerializer(book_obj, many=many).data
        }, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        book_id = request.data.get('user_id')
        print(book_id)
        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get('ids')
        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if response:
            return Response({
                'message': '删除成功'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': '删除失败或者图书不存在'
            }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)
        book_id = request.data.get('user_id')
        print(book_id)
        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'message': '修改的图书不存在'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = BookDeModelSerializer(data=request_data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer_save = serializer.save()
        return Response({
            'message': '修改成功',
            'result': BookModelSerializer(serializer_save).data
        }, status=status.HTTP_200_OK)
