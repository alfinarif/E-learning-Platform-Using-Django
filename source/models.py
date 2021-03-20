from django.db import models
from django.urls import reverse


class Project(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    pro_img = models.ImageField(upload_to='pro_img')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=255)
    sourse_code = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='lesson_img')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail',
                       kwargs={
                           'course_slug': self.course.slug,
                           'lesson_slug': self.slug
                       })
