import csv
import redis
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .form_data import to_json, to_geojson_line, to_geojson_point
from .positon_analysis import point_in_polygon, point_in_fenqu

from DataAnalysis.settings import POOL


def load_data():
    filename = "static/data/sharedbike.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        head_row = next(reader)
        conn = redis.Redis(connection_pool=POOL)
        for row in reader:
            id = row[0]
            print(id)
            start_point = [float(row[5]), float(row[6])]
            end_point = [float(row[8]), float(row[9])]
            if point_in_polygon(start_point, "hangzhou.json") and point_in_polygon(end_point, "hangzhou.json"):
                conn.set(name=id, value=to_json(row, "",
                                                point_in_fenqu(start_point),
                                                point_in_fenqu(end_point)))


def home(request):
    # load_data()
    return render(request, "Main/Home.html")


def get_all_points(request):
    result = to_geojson_line(list(range(3140202, 3592812)))
    return JsonResponse(result)


def get_start_points(request):
    result = to_geojson_point(list(range(3140202, 3592812)), True)
    lst = [[0 for i in range(1378)] for i in range(2378)]
    for feature in result["features"]:
        x = feature["geometry"]["coordinates"][0]
        y = feature["geometry"]["coordinates"][1]
        x = float(x)
        y = float(y)
        x = int(x * 1000 - 118344)
        y = int(y * 1000 - 29189)
        lst[x][y] += 1
    return JsonResponse(lst)


