from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'source/courses.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'



class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'source/single-course.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'


class LessonDetailView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course_qs = Project.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()

        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()
            obj = course.lessons.all()

        context = {
            'object': lesson,
            'obj': obj
        }
        return render(request, 'source/single-course.html', context)
