from django.contrib import include, admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myhole/', include('music urls')),
               
]
