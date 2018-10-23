from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from .models import Chauffeur, Taxi, Permission


class ChauffeurForm(ModelForm):
    model = Chauffeur
    readonly = ('permission_id',)
    fields = '__all__'



class PermissionForm(ModelForm): 
    class Meta:
        model = Permission
        fields = '__all__'
        widgets = {
            'permission_id' : forms.TextInput(attrs={'class': 'form-control'}),
            'chauffeur'     : forms.TextInput(attrs={'class':  'form-control'}),
            'taxi'          : forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut'    : forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'date_fin'      : forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'destination'   : forms.TextInput(attrs={'class':'form-control'}),
            }
    

