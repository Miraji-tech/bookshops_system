from django import forms
from .models import book_shop


class book_shopsForm(forms.ModelForm):
    class Meta:
        model = book_shop
        fields = ('book_shop_name', 'location', 'owner')
