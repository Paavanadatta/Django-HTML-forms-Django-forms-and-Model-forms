from django import forms
from demo2.validators import *

class registerform(forms.Form):
    username=forms.CharField(validators=[namelength])
    password=forms.CharField(widget=forms.PasswordInput,validators=[namelength])
    email=forms.EmailField()
    phone=forms.IntegerField(validators=[phonelength])
