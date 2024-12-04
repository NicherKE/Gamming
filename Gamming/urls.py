from django.contrib import admin
from django.urls import path
from Gamming import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('browse/',views.browse),
    path('details/',views.details),
    path('streams/',views.streams),
    path('profile/',views.profile),
    path('login/',views.login),
    path('registration/',views.sign,name='registration'),
    path('adminmain/',views.adminmain),
    path('user/',views.user),
    path('userlist/',views.list),
    path('trending/',views.trending),
    path('gamelist/',views.gamelist),
    path('addgame/',views.addgame),
    path('del/',views.delete),


]
