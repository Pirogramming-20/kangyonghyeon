from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm


# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    ctx = {"ideas": ideas}
    return render(request, "idea/idea_list.html", ctx)


def create(request):
    if request.method == "GET":
        form = IdeaForm()
        ctx = {"form": form}
        return render(request, "idea/idea_create.html", ctx)
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect("idea:main")


def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {"idea": idea}
    return render(request, "idea/idea_detail.html", ctx)


def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == "GET":
        form = IdeaForm(instance=idea)
        ctx = {"form": form, "pk": pk}
        return render(request, "idea/idea_update.html", ctx)
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect("idea:detail", pk)


def delete(request, pk):
    if request.method == "POST":
        Idea.objects.get(id=pk).delete()
    return redirect("idea:main")
