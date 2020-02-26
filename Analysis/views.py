import json, redis, math

from django.shortcuts import render
from django.http import JsonResponse
from DataAnalysis.settings import POOL

conn = redis.Redis(connection_pool=POOL)


# Create your views here.


def get_home(request):
    return render(request, "Analysis/grid_heatmap.html")


def get_trajectory_lenses(request):
    return render(request, "Analysis/trajectory_lenses.html")


def get_info_by_id(request):
    if request.method == "POST":
        id = request.POST['id']
        if conn.exists(id):
            info = eval(conn.get(id))
            id_list = []
            for i in info:
                id_list.append(i['id'])
            dis_list = [0 for i in range(10)]
            time_list = [0 for i in range(12)]
            rose_list = [[0 for i in range(16)] for i in range(6)]

            for i in id_list:
                if conn.exists(i):
                    try:
                        path = eval(conn.get(i))
                        angle = azimuthAngle(path['DepartLongitude'], path['DepartLatitude'], path['ArriveLongitude'],
                                             path['ArriveLatitude'])
                        if path["distance"] >= 4.5:
                            dis_list[9] += 1
                            rose_list[5][int(angle // 22.5)] += 1
                        else:
                            dis_list[int(path["distance"] * 2)] += 1
                            if path['distance'] < 0.5:
                                rose_list[0][int(angle // 22.5)] += 1
                            else:
                                rose_list[int(path["distance"] + 0.5)][int(angle // 22.5)] += 1
                        time_list[int(path["DepartTime"].split(":")[0].split(" ")[-1]) // 2 - 1] += 1
                    except:
                        continue
            return JsonResponse({
                'data': info,
                'dis_list': dis_list,
                'time_list': time_list,
                'rose_list': rose_list,
            })
        else:
            return JsonResponse({
                'data': [],
                'dis_list': [],
                'time_list': []
            })


def azimuthAngle(x1, y1, x2, y2):
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 > x1 and y2 < y1:
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1:
        angle = math.pi + math.atan(dx / dy)
    elif x2 < x1 and y2 > y1:
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return (angle * 180 / math.pi)
