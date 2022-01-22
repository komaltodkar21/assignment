from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    username=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=70)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=70)
    created_at = models.DateField()
    updated_at = models.DateField()