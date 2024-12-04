from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UpdateUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists() and username != self.instance.username:
            raise forms.ValidationError('This username is already taken.')
        return username


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image']

