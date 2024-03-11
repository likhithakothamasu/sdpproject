
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('login/',views. login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login1/', views.login1, name='login1'),
    path('signup1/', views.signup1, name='signup1'),
    path('logout/', views.logout, name='logout'),
    path('donate/',views.donate,name='donate'),
    path('urgent/',views.urgent,name='urgent'),
    path('animals/',views.animals,name='animals'),
    path('children/',views.children,name='children'),
    path('hungry/',views.hungry,name='hungry'),
    path('disability/',views.disability,name='disability'),
    path('medical/',views.medical,name='medical'),
    path('education/',views.education,name='education'),
    path('women/',views.women,name='women'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
]


