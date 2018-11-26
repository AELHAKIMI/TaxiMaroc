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
    error_css_class = 'error'
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
    error_css_class = 'error'
    permis = forms.CharField(
        required = True,
        label    = 'Numero de Permis',
        widget   = forms.TextInput(attrs={'class': 'form-control',}),
        

    )
    nom          = forms.CharField(
        required = False,
        label    = 'Nom',
        widget   = forms.TextInput(attrs={'class': 'form-control',})

    )
    type_permis  = forms.ChoiceField(
        choices  = (
            ('',  '----------',),
            ('1', 'Grand Taxi',),
            ('2', 'Petit Taxi',), 
        ),
        required= False,
        label   = 'Type de permis',
        widget  = forms.Select(attrs={'class': 'form-control'})
    )
    sexe        = forms.ChoiceField(
        choices = (
            ('',  '--------',),
            ('F', 'FEMININ',),
            ('M', 'MASCULIN',),
            ('I', 'INDETERMINE',),
        ),
        required= False,
        label   = 'Sexe',
        widget  = forms.Select(attrs={'class': 'form-control'})
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
    cin = forms.CharField(
        required = False,
        label   = 'CIN',
        widget  = forms.TextInput(attrs={'class': 'form-control',}),
    )

    visite_medicale_min = forms.DateField(
        input_formats=[
            '%d%m%Y',
            '%d/%m/%Y',
            '%d%m%y',
            '%d/%m/%y'
        ],
        required = False,
        label    = 'Visite medicale',
        widget   = forms.DateInput(attrs={'class': 'form-control',})

    )
    visite_medicale_max = forms.DateField(
        input_formats=[
            '%d%m%Y',
            '%d/%m/%Y',
            '%d%m%y',
            '%d/%m/%y'
        ],
        required    = False,
        label       = "Jusqu' ",
        widget      = forms.DateInput(attrs={'class': 'form-control',})

    )

    num_telephone = forms.CharField(
        required = False,
        label    = 'Telephone',
        widget   = forms.TextInput(attrs={'class': 'form-control',})
    )
    isActive    = forms.BooleanField(
        required= False,
        label   = 'Active',
        
        widget  = forms.CheckboxInput(attrs={'class': ''}, check_test=None) 
    )
    def clean_sexe(self):
        return self.cleaned_data['sexe']


############################################# Taxi Forms

class TaxiForm(ModelForm):
    class Meta:
        model = Taxi
        fields = '__all__'
        widgets = {
            'numero_taxi' : forms.TextInput(attrs={'class': 'form-control',}),
            'type_taxi'   : forms.Select(attrs={'class': 'form-control',}),
            'matricule' : forms.TextInput(attrs={'class': 'form-control',}),
            'agrement' : forms.TextInput(attrs={'class': 'form-control',}),
            'Marque' : forms.TextInput(attrs={'class': 'form-control',}),
            'modele' : forms.TextInput(attrs={'class': 'form-control',}),
            'assurance' : forms.DateInput(attrs={'class': 'form-control',}),
            'visite_technique': forms.DateInput(attrs={'class': 'form-control',}),

        }