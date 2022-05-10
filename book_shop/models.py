from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class book_shop(models.Model):
    book_shop_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.book_shop_name