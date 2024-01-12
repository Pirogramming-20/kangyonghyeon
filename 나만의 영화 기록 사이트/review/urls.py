from django.urls import path, include
from .views import *

urlpatterns=[
  path('',review_list),
  path('create',review_create),
  path('<int:pk>',review_read),
  path('<int:pk>/update', review_update),
  path('<int:pk>/delete',review_delete),
]
