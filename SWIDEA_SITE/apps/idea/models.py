from django.db import models
from apps.tool.models import Tool


# Create your models here.
class Idea(models.Model):
    title = models.CharField("아이디어명", max_length=30)
    image = models.ImageField("Image", null=True)
    content = models.TextField("아이디어 설명")
    interest = models.IntegerField("아이디어 관심도", default=0)
    created_date = models.DateTimeField("작성일", auto_now_add=True)
    updated_date = models.DateTimeField("수정일", auto_now=True)

    def __str__(self):
        return self.title

    tool = models.ForeignKey(Tool,
                             verbose_name="예상 개발툴",
                             on_delete=models.SET_NULL,
                             null=True)

    # ideaStar따로 추가하기
