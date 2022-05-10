from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class add_userForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(add_userForm, self).__init__(*args, **kwargs)

        for fieldnames in ['username', 'password1', 'password2']:
            self.fields[fieldnames].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
