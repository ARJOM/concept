from django import forms

from .models import UUIDUser


# User: create
class UUIDUserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(UUIDUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = UUIDUser
        form = forms.ModelForm
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Login',
            'email': 'Email',
            'password': 'Password',
        }
