from django.urls import path
from .views import ProjectListView, ProjectDetailView, LessonDetailView

urlpatterns = [
    path('list', ProjectListView.as_view(), name='list'),
    path('<slug>', ProjectDetailView.as_view(), name='detail'),
    path('<course_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson-detail'),
]