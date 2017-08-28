from rest_framework.serializers import ModelSerializer
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ..models import Location


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        geo_field = "point"
        fields = ('id', 'location_name', 'point')
