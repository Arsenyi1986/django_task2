from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Note(models.Model):
    note_text = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

