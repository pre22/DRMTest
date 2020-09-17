from rest_framework import viewsets
from TodoApi.serializers import HeroSerializer
from TodoApi.models import Hero

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
