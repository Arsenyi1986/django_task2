from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass

    def new_user(self, data):
        user = User()
        User.username = data['username']
        User.first_name = data['first_name']
        User.last_name = data['last_name']
        User.email = data['email']
        User.password = data['password1']
         # = data['password2']


class Note(models.Model):
    note_text = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
