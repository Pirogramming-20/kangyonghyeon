from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import default_storage

# Create your views here.
def review_list(request):
  movies=Movie.objects.all()
  context={
    'movies':movies
  }
  #context는 뷰에서 테플릿으로 데이터를 전달하는 변수
  return render(request,'movie_list.html',context)

def review_create(request):
  if request.method=='POST':
    Movie.objects.create(
      title=request.POST['title'],
      year=request.POST['year'],
      genre=request.POST['genre'],
      star=request.POST['star'],
      time=request.POST['time'],
      review=request.POST['review'],
      director=request.POST['director'],
      actor=request.POST['actor'],
      poster=request.FILES['poster'],
    )
    return redirect('/review')
  return render(request,'review_create.html')

def review_read(request,pk):
  review=Movie.objects.get(id=pk)
  hour,minutes=divmod(review.time,60)
  context={
    'review':review,
    'hour':hour,
    'minutes':minutes,
  }
  return render(request,'review_read.html',context)

def review_update(request,pk):
  review=Movie.objects.get(id=pk)
  if request.method =="POST":
    review.title=request.POST['title']
    review.year=request.POST['year']
    review.genre=request.POST['genre']
    review.star=float(request.POST['star'])
    review.time=request.POST['time']
    review.review=request.POST['review']
    review.director=request.POST['director']
    review.actor=request.POST['actor']
    if 'poster' in request.FILES:
      if review.poster:
          default_storage.delete(review.poster.path)
      review.poster = request.FILES['poster']
    review.save()
    return redirect(f'/review/{pk}')
  #save는 튜플을 받을수 없어서 딕셔너리 형태로 할당해서 저장한다
  context={
    'review':review
  }
  return render(request,'review_update.html',context)

def review_delete(request,pk):
  if request.method=="POST":
    review=Movie.objects.get(id=pk)
    review.delete()
  return redirect('/review')
