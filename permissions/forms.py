from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from .models import Chauffeur, Taxi, Permission
from django.utils.html import format_html
from dal import autocomplete


class ChauffeurForm(ModelForm):
    model = Chauffeur
    readonly = ('permission_id',)
    fields = '__all__'




class PermissionForm(ModelForm): 
    chauffeur = forms.ModelChoiceField(
         queryset=Chauffeur.objects.all(),
         widget=autocomplete.ModelSelect2(url='chauffeur-autocomplete', attrs={'class': 'form-control'}),
    )
    taxi = forms.ModelChoiceField(
        queryset    = Taxi.objects.all(),
        widget      = autocomplete.ModelSelect2(url='taxi-autocomplete',attrs={'class': 'form-control'} ),
    )
    class Meta:
        model = Permission
        fields = '__all__'
        widgets = {
            'permission_id'     : forms.TextInput(attrs={'class': 'form-control'}),          
            'taxi'              : forms.TextInput(attrs={'class': 'form-control'}),
            'date_permission'   : forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'destination'       : forms.TextInput(attrs={'class': 'form-control'}),
            'duree_permission'  : forms.TextInput(attrs={'class': 'form-control'}),
            'periode_permission': forms.Select(attrs={'class':'form-control'}),
            }
    

