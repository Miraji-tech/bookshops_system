from django import forms
from .models import books
from django.contrib.auth.models import User


class bookForm(forms.ModelForm):

    created_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = books
        fields = ('book_name', 'author', 'item', 'price', 'book_category', 'bookshop', 'book_image', 'created_by')
