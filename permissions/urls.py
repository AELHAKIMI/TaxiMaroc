from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index-view' ),
    url(r'^permission/$', views.PermissionListView.as_view(),name='permission-list-view'),
    url(r'^permission/add', views.PermissionCreateView.as_view(), name='permission-create-view'),
    url(r'^permission/(?P<pk>[0-9]+)/$', views.PermissionDetailView.as_view(), name='permission-detail-view'),
    url(r'^permission/(?P<pk>[0-9]+)/change$', views.PermissionUpdateView.as_view(), name='permission-update-view'),
    url(r'^permission/(?P<pk>[0-9]+)/delete$', views.PermissionDeleteView.as_view(),name='permission-delete-view'),
    url(
        r'^chauffeur-autocomplete/$',
        views.ChauffeurAutocompleteView.as_view(),
        name='chauffeur-autocomplete',
    ),
    url(
        r'^taxi-autocomplete/$',
        views.TaxiAutocompleteView.as_view(),
        name='taxi-autocomplete',
    ),
  
]