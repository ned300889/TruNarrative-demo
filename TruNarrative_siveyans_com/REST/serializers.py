from rest_framework import serializers
from .models import people

class peopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = people
        fields = ('name', 'alias')
