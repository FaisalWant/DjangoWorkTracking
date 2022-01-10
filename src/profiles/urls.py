
from django.urls import path
from django.conf import settings
from .views import profile_view



app_name='profiles'


urlpatterns = [
    path('',profile_view, name='profile_view'),
]
