from django.db import models

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
#내가 웹사이트에서 입력한 텍스트

# Create your models here.
