from django.test import TestCase, Client
from django.urls import reverse
from source.models import Project, Lesson
import json


class TestViews(TestCase):
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('list'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'source/courses.html')
