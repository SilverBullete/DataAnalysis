from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name="Analysis/grid_heatmap.html")),
    path('', views.get_home),
    path('trajectory_lenses', views.get_trajectory_lenses),
    path('get_info', views.get_info_by_id)
]
