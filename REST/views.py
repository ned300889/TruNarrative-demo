from rest_framework import viewsets
from .serializers import peopleSerializer
from .models import people

class peopleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = people.objects.all().order_by('name')
    serializer_class = peopleSerializer
