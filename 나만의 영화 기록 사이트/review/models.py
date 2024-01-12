from django.db import models

# Create your models here.
class Movie(models.Model):
  title=models.CharField(max_length=32)
  year=models.CharField(max_length=32)
  #year을 숫자로 받는게 나으려나?
  genre=models.CharField(max_length=32)
  star=models.FloatField()
  poster = models.ImageField(null=True)
  time=models.IntegerField()
  review=models.TextField()
  director=models.CharField(max_length=32)
  actor=models.CharField(max_length=32) 
  #pillow패키지 설치 알리기.




