from django.urls import path
from .views import *

app_name = "tool"

urlpatterns = [
    path("list/", tool_list, name="tool_list"),
    path("create/", tool_create, name="tool_create"),
    path("detail/<int:pk>/", tool_detail, name="tool_detail"),
    path("delete/<int:pk>", tool_delete, name="tool_delete"),
    path("update/<int:pk>/", tool_update, name="tool_update"),
]
