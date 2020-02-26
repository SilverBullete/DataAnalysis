from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_map_home),
    path('heatmap/start_heatmap', views.get_start_heatmap),
    path('heatmap/end_heatmap', views.get_end_heatmap),
    path('scatter/start_scatter', views.get_start_scatter),
    path('scatter/end_scatter', views.get_end_scatter),
]
