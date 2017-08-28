from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import contentType
from faker import faker
from rest_framework.test import APITestCase
from test_plus.test import TestCase
from ..factories import LocationFactory
from ..apis import serializers


class BaseAPITestCase(APITestCase, TestCase):

    def seUp(self):
        self.location = LocationFactory()
        self.user = self.make_user()
        self.user.active = True
        self.faker = Faker()


class LocationTestCase(BaseAPITestCase):

    def setup(self):
        super(LocationTestCase, self).setUp()
        self.location = LocationFactory()

    def test_list(self):
        url = reverse('location_api:location-list')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 401)

        with self.login(self.user):
            response = self.client.get(url, format='json')
            import pdb; pdb.set_trace()
