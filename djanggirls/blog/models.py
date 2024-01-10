from django.conf import settings
from django.db import models
#django 패키지에서 불러온다
from django.utils import timezone

#매개변수를 models.Model로 하면서 장고 데이터 베이스에 저장
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #위에서 부터 링크,타이틀글자수,글적는부분,날짜&시간

    def publish(self):
        self.published_date = timezone.now()
        self.save()
      #publish시간 알려줌
    def __str__(self):
        return self.title
    #title리턴