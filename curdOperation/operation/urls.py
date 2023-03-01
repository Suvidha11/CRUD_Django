from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.display,name="display"),
    path('add',views.add,name="add"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    
]