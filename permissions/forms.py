from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from .models import Chauffeur, Taxi, Permission


class ChauffeurForm(ModelForm):
    model = Chauffeur
    readonly = ('permission_id',)
    fields = '__all__'

class PermissionForm(ModelForm):
    # chauffeur = forms.ModelChoiceField(queryset=Chauffeur.objects.all(), widget=forms.TextInput())
    
    class Meta:
        model = Permission
        fields = '__all__'
        widgets = {
            'permission_id' : forms.TextInput(attrs={'class': 'form-control'}),
            'destination'   : forms.TextInput(attrs={'class':'form-control'}),
            'date_debut'    : forms.DateInput(attrs={'class': 'datepicker'}),
            'chauffeur'     : forms.Select(attrs={'class': 'selectpicker'})
        }
    

