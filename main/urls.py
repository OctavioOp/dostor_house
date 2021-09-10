from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),
    path('new_appointment', views.new_appointment),
    path('delete_appointment/<id_r>', views.delete_appointment)
]
