from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index-view' ),
    ############################# Permission Urls
    url(r'^permission/$', views.PermissionListView.as_view(),name='permission-list-view'),
    url(r'^permission/add$', views.PermissionCreateView.as_view(), name='permission-create-view'),
    url(r'^permission/(?P<pk>[0-9]+)/$', views.PermissionDetailView.as_view(), name='permission-detail-view'),
    url(r'^permission/(?P<pk>[0-9]+)/change$', views.PermissionUpdateView.as_view(), name='permission-update-view'),
    url(r'^permission/(?P<pk>[0-9]+)/delete$', views.PermissionDeleteView.as_view(),name='permission-delete-view'),
    url(
        r'^chauffeur-autocomplete/$',
        views.ChauffeurAutoCompleteView.as_view(),
        name='chauffeur-autocomplete',
    ),
    url(
        r'^taxi-autocomplete/$',
        views.TaxiAutoCompleteView.as_view(),
        name='taxi-autocomplete',
    ),

    ############################## Chauffeurs Urls
    url(r'^chauffeur/$', views.ChauffeurListView.as_view(),name='chauffeur-list-view'),
    url(r'^chauffeur/(?P<pk>[0-9]+)/$', views.ChauffeurDetailView.as_view(), name='chauffeur-detail-view' ),
    url(r'^chauffeur/add/$', views.ChauffeurCreateView.as_view(), name='chauffeur-create-view'),
    url(r'^chauffeur/(?P<pk>[0-9]+)/change$', views.ChauffeurUpdateView.as_view(), name='chauffeur-update-view'),
    url(r'^chauffeur/(?P<pk>[0-9]+)/delete$', views.ChauffeurDeleteView.as_view(), name='chauffeur-delete-view'),
    url(r'^chauffeur/search/$', views.ChauffeurSearchList.as_view(), name='chauffeur-search-view'),
    ############################# Taxi Urls
    url(r'^taxi/$', views.TaxiListView.as_view(), name='taxi-list-view'),
    url(r'^taxi/(?P<pk>[0-9]+)/$', views.TaxiDetailView.as_view(), name='taxi-detail-view'),
    url(r'^taxi/add/$', views.TaxiCreateView.as_view(), name='taxi-create-view'),
    url(r'^taxi/(?P<pk>[0-9]+)/change$', views.TaxiUpdateView.as_view(), name='taxi-update-view'),
    url(r'^taxi/(?P<pk>[0-9]+)/delete$',views.TaxiDeleteView.as_view(), name='taxi-delete-view'),


  
]