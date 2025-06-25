
from django import forms

class CryptoForm(forms.Form):
    Open = forms.FloatField()
    High = forms.FloatField()
    Low = forms.FloatField()
    Close = forms.FloatField()
    Volume = forms.FloatField()
