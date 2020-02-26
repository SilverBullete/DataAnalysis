from django.shortcuts import render


# Create your views here.
def get_map_home(request):
    return render(request, "Map/map_analysis.html")


def get_start_heatmap(request):
    return render(request, "Map/start_heatmap.html")


def get_end_heatmap(request):
    return render(request, "Map/end_heatmap.html")


def get_start_scatter(request):
    return render(request, "Map/start_scatter.html")


def get_end_scatter(request):
    return render(request, "Map/end_scatter.html")

