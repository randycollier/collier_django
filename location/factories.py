import factory
import factory.fuzzy
import string
from .models import Location


class LoctionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Location

    location_name = factory.Faker('street_name')
