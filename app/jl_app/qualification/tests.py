from rest_framework import status
from rest_framework.test import APITestCase
from qualification.models import Passport, Qualification

from django.contrib.auth.models import User


class QualificationTests(APITestCase):
    def setUp(self):
        self.user = user = User.objects.create_user(
            username='user1',
            password=b'0123456'
        )

        self.data = {
            "first_name": "oleg",
            "last_name": "pavlov",
            "middle_name": "sergeevich",
            "serial_number": 123456789,
            "date_birth": "2008-11-25",
            "place_birth": "Moscow",
            "date_issue": "2015-02-02",
            "issued_by": 2,
            "registration_address": 2
        }

        self.client.force_authenticate(user=user)

    def test_init_qualification(self):
        url = '/api/v1/qualification/'

        response = self.client.get(url, format='json')

        if response.status_code != status.HTTP_201_CREATED:
            self.assertEqual(
                response.status_code, status.HTTP_200_OK,
                msg=response.json()
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Qualification.objects.count(), 1)

    def test_add_passport(self):
        Qualification.objects.create(user=self.user)

        url = '/api/v1/qualification/passport/'

        response = self.client.post(url, self.data, format='json')

        if response.status_code != status.HTTP_201_CREATED:
            self.assertEqual(
                response.status_code, status.HTTP_200_OK,
                msg=response.json()
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passport.objects.count(), 1)
        self.assertEqual(Qualification.objects.count(), 1)

        qualification = Qualification.objects.get(user=self.user)

        self.assertEqual(
            qualification.user.passport.serial_number, 123456789
        )

    def test_update_confirm_qualification(self):
        url = '/api/v1/qualification/confirm/'

        Qualification.objects.create(user=self.user, confirm_rules=0)

        data = {
            "confirm_rules": 1
        }

        response = self.client.put(url, data, format='json')

        if response.status_code != status.HTTP_200_OK:
            self.assertEqual(
                response.status_code, status.HTTP_200_OK,
                msg=response.json()
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Qualification.objects.count(), 1)

        qualification = Qualification.objects.get(user=self.user)
        self.assertEqual(qualification.confirm_rules, 1)

    def test_get_confirm_qualification(self):
        url = '/api/v1/qualification/confirm/'

        Qualification.objects.create(user=self.user, confirm_rules=1)

        response = self.client.get(url, format='json')

        if response.status_code != status.HTTP_200_OK:
            self.assertEqual(
                response.status_code, status.HTTP_200_OK,
                msg=response.json().confirm_rules
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Qualification.objects.count(), 1)
        self.assertEqual(response.json(), {'confirm_rules': True})

    def test_update_status_qualification(self):
        url = '/api/v1/qualification/status/'

        Qualification.objects.create(user=self.user, status=0)

        data = {
            'status': 1
        }

        response = self.client.put(url, data, format='json')

        if response.status_code != status.HTTP_200_OK:
            self.assertEqual(
                response.status_code, status.HTTP_200_OK,
                msg=response.json()
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Qualification.objects.count(), 1)

        qualification = Qualification.objects.get(user=self.user)
        self.assertEqual(qualification.status, 1)

    def test_get_status_qualification(self):
        url = '/api/v1/qualification/status/'

        Qualification.objects.create(user=self.user, status=1)

        response = self.client.get(url, format='json')

        if response.status_code != 200:
            self.assertEqual(
                response.status_code, status.HTTP_200_OK,
                msg=response.json()
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Qualification.objects.count(), 1)
        self.assertEqual(response.json(), {'status': True})
