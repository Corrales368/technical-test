# Import django
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Import self app
from apps.student.models import Student


class StudentViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(
            user_id=1
        )

    def test_list_students(self):
        url = reverse('studentmodel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_student(self):
        url = reverse('studentmodel-list')
        data = {'user': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_retrieve_student(self):
        url = reverse('studentmodel-detail', args=[self.student.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 1)

    def test_update_student(self):
        url = reverse('studentmodel-detail', args=[self.student.pk])
        data = {'user': 2}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get(pk=self.student.pk).user_id, 2)

    def test_delete_student(self):
        url = reverse('studentmodel-detail', args=[self.student.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)
