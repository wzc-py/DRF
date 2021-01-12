from django.urls import path
from lastapp import views

urlpatterns = [
    path("book/",views.BookGenericAPIView.as_view()),
    path("book/<str:id>/",views.BookGenericAPIView.as_view()),

]