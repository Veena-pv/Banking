from .import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('regform', views.regform, name='regform'),
    path('register1', views.register1, name='register1'),
 ]