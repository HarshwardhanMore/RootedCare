from django.urls import path

from . import views

urlpatterns = [
    path('', views.owner),
    path('owner', views.owner),
    path('caretaker', views.caretaker),
]
