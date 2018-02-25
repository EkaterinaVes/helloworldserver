from django import forms
    
class HelloForm(forms.Form):
    hello = forms.CharField(help_text="Enter your NAME")