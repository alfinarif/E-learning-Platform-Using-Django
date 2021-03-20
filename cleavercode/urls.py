from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Index, Contact, Course, Details
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('contact', Contact, name='contact'),
    path('course', Course, name='course'),
    path('details', Details, name='details'),
    path('', include('account.urls')),
    path('', include('source.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)