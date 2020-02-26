import json


from DataAnalysis.settings import BASE_DIR


def point_in_fenqu(point):
    filename = BASE_DIR + "/static/data/fenqu.json"
    gfn = open(filename, 'r', encoding='utf-8')
    gjson = json.load(gfn)
    polygons = gjson["features"]
    for polygon in polygons:
        if is_poi_within_poly(point, polygon["geometry"]['coordinates'][0]):
            return polygon["properties"]["name"]


def point_in_polygon(point, file):
    filename = BASE_DIR + "/static/data/" + file
    gfn = open(filename, 'r', encoding='utf-8')
    gjson = json.load(gfn)
    polygon = gjson["features"][0]["geometry"]['coordinates']
    gfn.close()
    return is_poi_within_poly(point, polygon)


def is_poi_within_poly(poi, poly):
    sinsc = 0
    for epoly in poly:
        for i in range(len(epoly) - 1):
            s_poi = epoly[i]
            e_poi = epoly[i + 1]
            if is_ray_intersects_segment(poi, s_poi, e_poi):
                sinsc += 1

    return True if sinsc % 2 == 1 else  False


def is_ray_intersects_segment(poi, s_poi, e_poi):
    if s_poi[1] == e_poi[1]:
        return False
    if s_poi[1] > poi[1] and e_poi[1] > poi[1]:
        return False
    if s_poi[1] < poi[1] and e_poi[1] < poi[1]:
        return False
    if s_poi[1] == poi[1] and e_poi[1] > poi[1]:
        return False
    if e_poi[1] == poi[1] and s_poi[1] > poi[1]:
        return False
    if s_poi[0] < poi[0] and e_poi[1] < poi[1]:
        return False

    xseg = e_poi[0] - (e_poi[0] - s_poi[0]) * (e_poi[1] - poi[1]) / (e_poi[1] - s_poi[1])
    if xseg < poi[0]:
        return False
    return True
