from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    self_prove = models.CharField(max_length=50)
    self_prove_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class CustomerMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.subject


class NewsAgreedCustomer(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "Subscribed Customer"
