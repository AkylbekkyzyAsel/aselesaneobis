from rest_framework import serializers
from .models import QuickStart

class QuickStartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuickStart
        fields = ('id', 'name', 'paradigm')


