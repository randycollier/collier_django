import pytest

from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker
from rest_framework.test import APITestCase
from test_plus.test import TestCase
from ..factories import LocaionFactory


class BaseAPITestCase(APITestCase, TestCase):

    def setUp(self):
        self.Location = LocaionFactory()
        self.user = self.make_user()
        self.user.active = True
        self.faker = Faker()


class LocationTestCase(BaseAPITestCase):

    def setUp(self):
        super(LocationTestCase, self).setUp()
        self.location = LocaionFactory()

    def test_list(self):
        url = reverse('locations_api:location-list')
        import pdb; pdb.set_trace()
        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 401)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(len(response.data), 0)
