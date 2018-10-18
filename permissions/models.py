from django.db import models

# Create your models here.


class Taxi(models.Model):
    numero_taxi = models.CharField(max_length=32, verbose_name='Numero Taxi')
    type_taxi   = models.ForeignKey(TypeTaxi, on_delete= models.PROTECT, verbose_name='Type Taxi')
    matricule   = models.CharField(max_length=32, verbose_name='Matricule')
    agrement    = models.CharField(max_length=32, verbose_name='Agrement')
    Marque      = models.CharField(max_length=128, vebose_name='Marque de vehicule')
    modele      = models.CharField(max_length=128, verbose_name='Modele de vehicule')
    assurance   = models.DateField(verbose_name='Date validite assurance')
    vite_technique  = models.DateField(verbose_name='Date validite Visite technique')

    class Meta:
        unique_otgether = ('numero_taxi', 'type_taxi')
