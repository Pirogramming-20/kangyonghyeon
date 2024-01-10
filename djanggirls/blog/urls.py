from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #mysite에서 연결된 urls을 post라는 뷰로 연결한다
]