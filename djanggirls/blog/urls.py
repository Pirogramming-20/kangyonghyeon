from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #mysite에서 연결된 urls을 post라는 뷰로 연결한다
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #pk키의 인덱스로 링크를 만든다 <>부분에서 장고는 정수값을 기대하고 pk라는 변수를 뷰로 전송한다
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]