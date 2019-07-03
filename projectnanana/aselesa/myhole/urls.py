from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myhole-home'),
    path('about/', views.about, name='myhole-about'),
]


