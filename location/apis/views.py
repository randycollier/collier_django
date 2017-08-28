from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
