from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #profle과 user 객체를 하나씩 연결
    #on_delete는 연결되어 있는 User 객체가 없어질 때, CASCADE는 profile도 없어지게 함
    #related_name은...
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    #unique = True, 닉네임은 하나가 유일해야 함
    message = models.CharField(max_length=100, null=True)