import json, redis

from django.shortcuts import render


def home(request):
    return render(request, "Chart/chart_analysis.html")


def get_bubble(request):
    return render(request, "Chart/bubble.html")


def get_line(request):
    return render(request, "Chart/line.html")


def get_column(request):
    return render(request, "Chart/column.html")


def get_chord(request):
    return render(request, "Chart/chord.html")


def get_start_sun(request):
    return render(request, "Chart/start_sun.html")


def get_end_sun(request):
    return render(request, "Chart/end_sun.html")