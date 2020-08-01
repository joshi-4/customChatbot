from django.urls import path
from mainSite import views

urlpatterns = [
    path('', views.index, name= 'index'),
]
