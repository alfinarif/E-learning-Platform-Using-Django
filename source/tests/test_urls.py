from django.test import SimpleTestCase
from django.urls import reverse, resolve
from source import views


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func.view_class, views.ProjectListView)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, views.ProjectDetailView)

    def test_lesson_detail_url_is_resolved(self):
        url = reverse('lesson-detail', args=['slug','slug'])
        self.assertEqual(resolve(url).func.view_class, views.LessonDetailView)