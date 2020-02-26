import json, redis
import time

from DataAnalysis.settings import POOL

conn = redis.Redis(connection_pool=POOL)


def to_json(row, school, start_fenqu, end_fenqu):
    data = {
        "school": school,
        "start_fenqu": start_fenqu,
        "end_fenqu": end_fenqu,
        "CompanyId": row[1],
        "BicycleNo": row[2],
        "DepartTime": row[4],
        "DepartLongitude": float(row[5]),
        "DepartLatitude": float(row[6]),
        "ArriveTime": row[7],
        "ArriveLongitude": float(row[8]),
        "ArriveLatitude": float(row[9])
    }
    return json.dumps(data)


def to_geojson_point(data, start):
    result = {
        "type": "FeatureCollection",
        "features": []
    }
    if start:
        for id in data:
            if conn.exists(id):
                info = json.loads(conn.get(id).decode("utf-8"))
                result["features"].append({"type": "Feature",
                                           "geometry": {"type": "Point",
                                                        "coordinates": [info["DepartLongitude"], info["DepartLatitude"]]},
                                           "properties": {}
                                           })
    else:
        for id in data:
            if conn.exists(id):
                info = json.loads(conn.get(id).decode("utf-8"))
                result["features"].append({"type": "Feature",
                                           "geometry": {"type": "Point",
                                                        "coordinates": [info["ArriveLongitude"], info["ArriveLatitude"]]},
                                           "properties": {}
                                           })
    return result


def to_geojson_line(data):
    result = {
        "type": "FeatureCollection",
        "features": []
    }
    for id in data:
        if conn.exists(id):
            info = json.loads(conn.get(id).decode("utf-8"))
            result["features"].append({"type": "Feature",
                                       "geometry": {
                                           "type": "LineString",
                                           "coordinates": [
                                               [info["DepartLongitude"], info["DepartLatitude"]], [
                                           info["ArriveLongitude"], info["ArriveLatitude"]]
                                       ]
                                       },
                                       "properties": {}
                                       })
    return result
