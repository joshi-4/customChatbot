from django.urls import path
from mainSite import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('login/',views.login, name= 'login'),
    path('accounts/login/', views.login),
    path('logout/', views.logout, name= 'logout'),
    path('register/', views.register, name= 'register'),
    path('upload/', views.upload, name= 'upload'),
    path('download/', views.download_apk, name= 'download')
]
