from django import forms
from .models import Reg
class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields='__all__'
        widgets={'pwd':forms.PasswordInput(),}

class LoginForm(forms.Form):
    User=forms.CharField(max_length=20)
    Pwd=forms.CharField(widget=forms.PasswordInput())
