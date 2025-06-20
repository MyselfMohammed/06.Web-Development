from django import forms
from .models import *


class Concrete_Application(forms.ModelForm):
    class Meta():
        model=Concrete_Model
        fields=['Cement','Slag','Flyash','Water','Super_Plasticizer','Coarse_Aggregate','Fine_Aggregate','Curing_Age_in_Days']
