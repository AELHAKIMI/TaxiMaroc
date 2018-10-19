from django.db import models
from multiselectfield import MultiSelectField


#variables global ggt

type_taxi_choice = (
    ('1', 'Grand Taxi',),
    ('2', 'Petit Taxi',),        
)
Sexe_Choice = (
    ('F', 'FEMININ',),
    ('M', 'MASCULIN',),
    ('I', 'INDETERMINE',),
)
# Create your models here.


class Taxi(models.Model):
    
    numero_taxi     = models.CharField(max_length=32, verbose_name='Numero Taxi')
    type_taxi       = models.CharField(max_length=1, choices = type_taxi_choice, verbose_name='Type Taxi')
    matricule       = models.CharField(max_length=32, verbose_name='Matricule')
    agrement        = models.CharField(max_length=32, verbose_name='Agrement')
    Marque          = models.CharField(max_length=128, vebose_name='Marque de vehicule')
    modele          = models.CharField(max_length=128, verbose_name='Modele de vehicule')
    assurance       = models.DateField(verbose_name="Date d'assurance")
    vite_technique  = models.DateField(verbose_name='Date de Visite technique')
    isActive        = models.BooleanField(verbose_name='Activé', default=True)
    isPrivate       = models.BooleanField(verbose_name='Privé', default=False)


    class Meta:
        unique_otgether = ('numero_taxi', 'type_taxi')

    


class Chauffeur(models.Model):

    type_permis_choice = type_taxi_choice

    permis_chauffeur    = models.CharField(max_length=32, verbose_name=' Numero de Permis')
    type_permis         = MultiSelectField(choices=type_permis_choice,verbose_name='Type de permis')
    nom_chauffeur       = models.CharField(max_length=128, verbose_name='Nom')
    sexe_chauffeur      = models.CharField(max_length=1, choices=Sexe_Choice, verbose_name='Sexe')
    date_naissance      = models.DateField(verbose_name='Date de naissance')
    cin_chauffeur       = models.CharField(max_length=32, verbose_name='CIN')
    visite_medicale     = models.DateField(verbose_name='Date de visite Medicale')
    num_telephone       = models.CharField(max_length=32, verbose_name='Numero Telephone')
    isActive            = models.BooleanField(verbose_name='Activé', default=True)
    isPrivate           = models.BooleanField(verbose_name='Privé', default=False)


class Permission(models.Model):
    chauffeur       = models.ForeignKey(Chauffeur, on_delete=models.PROTECT, verbose_name='Chauffeur')
    taxi            = models.ForeignKey(Taxi, on_delete=models.PROTECT, verbose_name='Taxi')
    date_debut      = models.DateTimeField(verbose_name='Date debut ')
    date_fin        = models.DateTimeField(verbose_name='Date fin')
    
    
