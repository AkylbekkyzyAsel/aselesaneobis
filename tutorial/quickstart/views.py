from django.shortcuts import render
from rest_framework import viewsets
from .models import QuickStart
from .serializers import QuickStartSerializer

class QuickStartView(viewsets.ModelViewSet):
    queryset = QuickStart.objects.all()
    serializer_class = QuickStartSerializer
