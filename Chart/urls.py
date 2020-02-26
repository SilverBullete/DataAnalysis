from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", views.home),
    path("bubble", views.get_bubble),
    path("line", views.get_line),
    path("column", views.get_column),
    path("chord", views.get_chord),
    path("sun/start_sun", views.get_start_sun),
    path("sun/end_sun", views.get_end_sun),
]