from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('', views.home),
    path('api/home_data', views.get_all_points),
    path('api/start_points', views.get_start_points)
]