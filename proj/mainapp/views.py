from django.shortcuts import render
from .models import User, Note

# Create your views here.


def regpage(request):
    if request.method == "GET":
        return render(request, "regpage.html")
    else:
        User.new_user(request.POST)


def loginpage(request):
    if request.method == "GET":
        return render(request, "loginpage.html")


def logoutpage(request):
    return render(request, "logoutpage.html")


def notespage(request):
    return render(request, "notespage.html")


def add_notepage(request):
    if request.method == "GET":
        return render(request, "add_notepage.html")


