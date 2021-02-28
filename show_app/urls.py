from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.allshows),
    path('shows/new', views.newshows),
    path('submitshow', views.submitshow),
    path('shows/<show_id>', views.show),
    path('shows/<show_id>/destroy', views.delete),
    path('shows/<show_id>/edit', views.edit),
    path('submitedit/<show_id>', views.submitedit)
]