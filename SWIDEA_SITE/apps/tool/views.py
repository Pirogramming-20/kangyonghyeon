from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm
from apps.idea.models import Idea

# Create your views here.


def tool_list(request):
    tools = Tool.objects.all()
    ctx = {"tools": tools}
    return render(request, "tool/tool_list.html", ctx)


def tool_create(request):
    if request.method == "GET":
        form = ToolForm()
        ctx = {"form": form}
        return render(request, "tool/tool_create.html", ctx)
    form = ToolForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        print("1234")
    return redirect("tool:tool_list")


def tool_detail(request, pk):
    tool = Tool.objects.get(id=pk)
    ideas = Idea.objects.filter(tool=tool)
    ctx = {"tool": tool, "ideas": ideas}
    return render(request, "tool/tool_detail.html", ctx)


def tool_update(request, pk):
    tool = Tool.objects.get(id=pk)
    if request.method == "GET":
        form = ToolForm(instance=tool)
        ctx = {"form": form, "pk": pk}
        return render(request, "tool/tool_update.html", ctx)
    form = ToolForm(request.POST, instance=tool)
    if form.is_valid():
        form.save()
    return redirect("tool:tool_detail", pk)


def tool_delete(request, pk):
    if request.method == "POST":
        Tool.objects.get(id=pk).delete()
    return redirect("tool:tool_list")
