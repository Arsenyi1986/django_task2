from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import User, Note

# Create your views here.


def reg_view(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'regpage.html', {'error': "Username is already taken"})
            else:
                user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
                                           password=make_password(password))
                user.save()
                login(request, user)
                return redirect("notes")
        else:
            return render(request, 'regpage.html', {'error': "Insert a matching password"})
    return render(request, "regpage.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("notes")
        else:
            return render(request, 'loginpage.html', {'error': "User does not exist"})
    return render(request, 'loginpage.html')


def logout_view(request):
    logout(request)
    return redirect("notes")


def notes_view(request):
    users = User.objects.all()
    if request.user in users:
        notes = Note.objects.filter(owner=request.user).order_by('-id')
        return render(request, "notespage.html", {'notes': notes})
    return render(request, "notespage.html")


def add_note_view(request):
    if request.method == "POST":
        note_text = request.POST.get('note-text')
        if note_text:
            note = Note.objects.create(note_text=note_text, owner=request.user)
            note.save()
            return redirect("notes")
        else:
            return render(request, "add_notepage.html", {'error': "Please write a note"})
    return render(request, "add_notepage.html")
