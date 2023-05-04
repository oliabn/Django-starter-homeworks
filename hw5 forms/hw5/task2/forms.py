from django import forms
from .models import User


class AuthorizationForm(forms.Form):
    """User authorization form.
    Authorization by user_name, email, and password"""

    user_name = forms.CharField(label="User name")
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=8,
                               widget=forms.PasswordInput())


class UserAuthorizationForm(forms.ModelForm):
    """User authorization form.
    Authorization by email and password"""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = User
        # fields = '__all__'

        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.TextInput(attrs={'class': 'form-input'})
        }
