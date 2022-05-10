from django.db import models
from category.models import category
from book_shop.models import book_shop
from django.contrib.auth.models import User


# Create your models here.
class books(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    # level = models.CharField(max_length=200)
    # curriculum = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to="images/", null=True, blank=True)
    item = models.IntegerField()
    price = models.IntegerField()
    book_category = models.ForeignKey(category, default='', on_delete=models.CASCADE)
    bookshop = models.ForeignKey(book_shop, default='', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.author
