from django import forms
def namelength(value):
    if not(3<=len(value)<=15):
        raise forms.ValidationError("Name should be more than 3 letters and less than 15 letters")

def phonelength(value):
    if not(len(str(value))==10):
        raise forms.ValidationError('Digits should be 10')
