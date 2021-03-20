from django.urls import path, include
from .views import Register, Login, Logout
urlpatterns = [
    path('register', Register, name='register'),
    path('login', Login, name='login'),
    path('logout', Logout, name='logout'),
]