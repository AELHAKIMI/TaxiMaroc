from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from .models import Chauffeur, Taxi, Permission
from django.utils.html import format_html
from dal import autocomplete





###################################### Permission Forms

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
    


####################################### Chauffeur Forms
class ChauffeurForm(ModelForm):
    class Meta:
        model = Chauffeur
        fields = '__all__'
        widgets = {
            'permis_chauffeur' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'type_permis'       : forms.CheckboxInput(attrs={'class':''}),
            'nom_chauffeur'     : forms.TextInput(attrs={'class': 'form-control'}),
            'sexe_chauffeur'   : forms.Select(attrs={'class': 'form-control'}),
            'date_naissance'    : forms.DateInput(attrs={'class': 'form-control'}),
            'cin_chauffeur'     : forms.TextInput(attrs={'class': 'form-control'}),
            'visite_medicale'   : forms.DateInput(attrs={'class': 'form-control'}),
            'num_telephone'     : forms.TextInput(attrs={'class': 'form-control'}),

        }
    
class ChauffeurSearchForm(forms.Form):
    permis = forms.CharField(
        required = False,
        label    = 'Numero de Permis',
        widget   = forms.TextInput(attrs={'class': 'form-control',})
    )
    nom     = forms.CharField(
        required = False,
        label    = 'Nom',
        widget   = forms.TextInput(attrs={'class': 'form-control',})

    )
    type_permis = forms.MultipleChoiceField(
        choices = (
            ('1', 'Grand Taxi',),
            ('2', 'Petit Taxi',), 
        ),
        required= False,
        label   = 'Type de permis',
        widget  = forms.CheckboxSelectMultiple(attrs={'class': ''})
    )
    sexe        = forms.MultipleChoiceField(
        choices = (
            ('F', 'FEMININ',),
            ('M', 'MASCULIN',),
            ('I', 'INDETERMINE',),
        ),
        required= False,
        label   = 'Sexe',
        widget  = forms.CheckboxSelectMultiple(attrs={'class': ''})
    )
    

    date_naissance_min = forms.DateField(
        input_formats=[
            '%d%m%Y',
            '%d/%m/%Y',
            '%d%m%y',
            '%d/%m/%y'
        ],
        required    = False,
        label       = 'Date naissance',
        widget      = forms.DateInput(attrs={'class': 'form-control',})

    )
    date_naissance_max = forms.DateField(
        input_formats=[
            '%d%m%Y',
            '%d/%m/%Y',
            '%d%m%y',
            '%d/%m/%y'
        ],
        required    = False,
        label       = "Jusuq' ",
        widget      = forms.DateInput(attrs={'class': 'form-control',})

    )
    def clean_sexe(self):
        return self.cleaned_data['sexe']