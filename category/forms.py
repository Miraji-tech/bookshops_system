from django import forms
from .models import category


class categoryForm(forms.ModelForm):
    
    class Meta:
        model = category
        fields = ('category_name',)
