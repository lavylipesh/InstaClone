from django import forms

class InstaForm(forms.Form):
    name = forms.CharField(label='Name',max_length=30)
    email = forms.EmailField(label='Email')