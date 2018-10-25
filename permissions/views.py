from django.shortcuts import render
from django.urls import reverse_lazy
from dal import autocomplete
from .models import Chauffeur, Taxi, Permission
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
from django.utils.html import format_html

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_permissions'
    def get_queryset(self):
        return Permission.objects.all()
############################ Chauffeur Views
chauffeur_titles = ('Permis', 'Nom', 'Date de naissance', 'CIN', 'Visite Medicale', 'Telephone')
class ChauffeurAutoCompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Chauffeur.objects.filter(isActive = True)
        if self.q:
            qs = qs.filter(nom_chauffeur__contains = self.q)
        return qs
    def get_result_label(self, item):
        return format_html('{}', item.nom_chauffeur)
    
    def get_selected_result_label(self, item):
        return item.permis_chauffeur + ' ' + item.nom_chauffeur

class ChauffeurListView(generic.ListView):
    template_name = 'chauffeur/chauffeurs.html'
    context_object_name = 'all_chauffeurs'
    def get_context_data(self, **kwargs):
        context = super(ChauffeurListView, self).get_context_data(**kwargs)
        context.update({
            'titles' : chauffeur_titles,
        })
        return context
    def get_queryset(self):
        return Chauffeur.objects.all()
class ChauffeurDetailView(generic.DetailView):
    model = Chauffeur
    context_object_name = 'chauffeur'
    template_name = 'chauffeur/chauffeurs.html'
    def get_context_data(self, **kwargs):
        context = super(ChauffeurDetailView, self).get_context_data(**kwargs)
        context.update({
            'titles' : chauffeur_titles,
        })
        return context

class ChauffeurCreateView(CreateView):
    model = Chauffeur
    fields = '__all__'
    template_name = 'chauffeur/chauffeur_form.html'

class ChauffeurUpdateView(UpdateView):
    model = Chauffeur
    fields = '__all__'
    template_name = 'chauffeur/chauffeur_form.html'

class ChauffeurDeleteView(DeleteView):
    model = Chauffeur
    success_url = reverse_lazy('index-view')
    template_name = 'chauffeur/confirm_delete.html'

############################# Taxi Views
class TaxiAutoCompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Taxi.objects.all()
        if self.q:
            qs = qs.filter(numero_taxi__contains = self.q)
        return qs
    def get_result_label(self, item):
        return format_html('{}', item)
    
    def get_selected_result_label(self, item):
        return str(item)

############################# Permission Views
permission_titles = ('Numero', 'Chauffeur', 'Taxi', 'Date', 'Destination', 'Duree', 'Periode')
class PermissionListView(generic.ListView):       
    template_name = 'permission/permissions.html'
    context_object_name = 'all_permissions'
    def get_context_data(self, **kwargs):
        context = super(PermissionListView, self).get_context_data(**kwargs)        
        context.update({            
            'titles': permission_titles,                                  
        })
        return context

    def get_queryset(self):
        return Permission.objects.all()

class PermissionCreateView(CreateView):
    model = Permission
    template_name = 'permission/permission_form.html'
    form_class = forms.PermissionForm



class PermissionDetailView(generic.DetailView):
    model = Permission 
    context_object_name = 'permission'    
    template_name = 'permission/permissions.html'
    def get_context_data(self, **kwargs):
        context = super(PermissionDetailView, self).get_context_data(**kwargs)        
        context.update({            
            'permission_titles': permission_titles,                                  
        })
        return context

class PermissionUpdateView(UpdateView):
    model = Permission
    fields = '__all__'
    template_name = 'permission/permission_form.html'

 
    # form_class = forms.PermissionForm

class PermissionDeleteView(DeleteView):
    model = Permission
    success_url = reverse_lazy('index-view')
    template_name = 'permission/confirm_delete.html'



    
