from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from modapp.models import Press, Book

# 出版社的序列化器
class PressModelSerializer(ModelSerializer):
    class Meta:
        model = Press
        fields = ("id", "press_name", "address")

# 图书的序列化器
class BookModelSerializer(ModelSerializer):
    publish = PressModelSerializer()

    class Meta:
        model = Book
        fields = ("book_name", "price", "pic", "publish", "create_time")
        extra_kwargs = {
            'publish': {
                'write_only': True
            },
            'authors': {
                'write_only': True
            },
            'publish_name': {
                'read_only': True
            },
            'publish_address': {
                'read_only': True
            }
        }

# 图书的反序列化器
class BookDeModelSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ("book_name", "price", "authors", "publish")

        extra_kwargs = {
            "book_name": {
                "min_length": 2,
                "max_length": 8,
                "required": True,
                "error_messages": {
                    "max_length": "字段不能超过8字符"
                }
            },
            "price": {
                "max_digits": 5,
                "decimal_places": 2,
            }
        }

    def validate(self, attrs):
        return attrs

    def validate_book_name(self, value):
        book = Book.objects.filter(book_name=value).first()

        if book:
            raise serializers.ValidationError("图书名已存在")
        return value

