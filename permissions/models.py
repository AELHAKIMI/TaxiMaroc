from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date
from multiselectfield import MultiSelectField
from django.urls import reverse


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

def foo():
    return increment_permission_id()


# Create your models here.
@python_2_unicode_compatible
class Taxi(models.Model):
    
    numero_taxi     = models.CharField(max_length=32, verbose_name='Numero Taxi')
    type_taxi       = models.CharField(max_length=1, choices = type_taxi_choice, verbose_name='Type Taxi')
    matricule       = models.CharField(max_length=32, verbose_name='Matricule')
    agrement        = models.CharField(max_length=32, verbose_name='Agrement')
    Marque          = models.CharField(max_length=128, verbose_name='Marque de vehicule')
    modele          = models.CharField(max_length=128, verbose_name='Modele de vehicule')
    assurance       = models.DateField(verbose_name="Date d'assurance")
    vite_technique  = models.DateField(verbose_name='Date de Visite technique')
    isActive        = models.BooleanField(verbose_name='Activé', default=True)
    isPrivate       = models.BooleanField(verbose_name='Privé', default=False)


    class Meta:
        unique_together = ('numero_taxi', 'type_taxi')
    
    def __str__(self):
        return self.numero_taxi 

    

@python_2_unicode_compatible
class Chauffeur(models.Model):

    type_permis_choice = type_taxi_choice

    permis_chauffeur    = models.CharField(max_length=32,unique=True, verbose_name=' Numero de Permis')
    type_permis         = MultiSelectField(choices=type_permis_choice,verbose_name='Type de permis')
    nom_chauffeur       = models.CharField(max_length=128, verbose_name='Nom')
    sexe_chauffeur      = models.CharField(max_length=1, choices=Sexe_Choice, verbose_name='Sexe')
    date_naissance      = models.DateField(verbose_name='Date de naissance')
    cin_chauffeur       = models.CharField(max_length=32,unique=True, verbose_name='CIN')
    visite_medicale     = models.DateField(verbose_name='Date de visite Medicale')
    num_telephone       = models.CharField(max_length=32, verbose_name='Numero Telephone',null=True, blank=True)
    isActive            = models.BooleanField(verbose_name='Activé', default=True)
    isPrivate           = models.BooleanField(verbose_name='Privé', default=False)

    def __str__(self):
        return self.permis_chauffeur + ' ' + self.nom_chauffeur + ' ' + ','.join(self.selected_typePermis_labels())

    def selected_typePermis_labels(self):
        return [label for value,label in type_taxi_choice if value in self.type_permis]
        
    
    
        

        
        
        

@python_2_unicode_compatible
class Permission(models.Model):
    
    permission_id   = models.CharField(max_length = 20, default = foo, editable=False , unique = True)
    chauffeur       = models.ForeignKey(Chauffeur, on_delete=models.PROTECT, verbose_name='Chauffeur')
    taxi            = models.ForeignKey(Taxi, on_delete=models.PROTECT, verbose_name='Taxi')
    date_debut      = models.DateTimeField(verbose_name='Date debut ')
    date_fin        = models.DateTimeField(verbose_name='Date fin')
    destination     = models.CharField(max_length=128, verbose_name='Destination',null=True, blank=True)

    def get_absolute_url(self):
        return reverse('permission-detail-view', kwargs={'pk': self.pk})


    def __str__(self):
        return str(self.permission_id) + ' ' + self.chauffeur.nom_chauffeur + ' ' + self.taxi.numero_taxi

def increment_permission_id():
    last_permission = Permission.objects.all().order_by('id').last()
    if not last_permission:
        return date.today().strftime('%y%m%d') + '0000'
    l_permission_id = last_permission.permission_id
    permission_int  = int(l_permission_id[6:10])
    new_permission_int  = permission_int + 1
    new_permission_id   = str(date.today().strftime('%y%m%d') + str(new_permission_int).zfill(4))
    return new_permission_id
    
