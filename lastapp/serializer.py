from rest_framework.serializers import ModelSerializer

from modapp.models import Book

class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","book_name","price","authors","pic","publish","create_time","publish_name","publish_address","author_list"]

        extra_kwargs = {
            "publish":{
                "write_only":True
            },
            "authors":{
                "write_only":True
            },
            "pic":{
                "read_only":True
            }
        }