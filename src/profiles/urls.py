
from django.urls import path
from django.conf import settings
from .views import test_view



app_name='profiles'


urlpatterns = [
    path('',test_view, name='test_view'),
]
