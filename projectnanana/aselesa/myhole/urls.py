from django.contrib import admin
from . import views

urlpatterns = [
               path('myhole/', views.index, name='index'),
               ]


