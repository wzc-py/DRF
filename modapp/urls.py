from django.urls import path

from modapp import views

urlpatterns=[
    path('check/',views.BookAPIView.as_view()),
    path('add/',views.BookAPIView.as_view()),
    path('check/<str:id>/',views.BookAPIView.as_view()),
    path('update/<str:id>/',views.BookAPIView.as_view()),
    path('update/',views.BookAPIView.as_view()),
]