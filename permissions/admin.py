from django.contrib import admin
from .models import Taxi, Chauffeur, Permission
from django import forms

# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    readonly_fields = ('permission_id',)    
    fields = ( 'permission_id','chauffeur','taxi', 'date_permission', 'destination', 'duree_permission','periode_permission',)
    raw_id_fields = ('chauffeur', 'taxi',)

    def get_fields(self, request, obj=None):
        fields = super(CustomAdmin, self).get_fields(request, obj)
        for field in fields:
            if field == 'permission_id' and obj is None:
                continue
            yield field

admin.site.register(Taxi)
admin.site.register(Chauffeur)
admin.site.register(Permission , CustomAdmin)



