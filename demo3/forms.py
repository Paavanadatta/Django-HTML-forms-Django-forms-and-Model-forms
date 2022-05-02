from wsgiref.validate import validator
from django import forms
from demo3.models import enqmodel
# from demo3.validator import *

#Create your forms here.
class enqform(forms.ModelForm):
    class Meta:
        model=enqmodel
        fields='__all__'
        #fields=['name','phone','email','address','desc']
        #fields=exclude['address']
    def clean(self):
        name=self.cleaned_data['name']
        if not(3<=len(name)<=15):
            raise forms.ValidationError("Name should be minimum 3 letters and maximum 15 letters")

        phone=self.cleaned_data['phone']
        if not(len(str(phone))==10):
            raise forms.ValidationError("Number should be 10 digits")

