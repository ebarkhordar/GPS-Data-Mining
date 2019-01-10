import csv
import os
import re
from data_utils.models import TaxiData, Location
from main_config import Config


def return_data_rows():
    path = os.path.dirname(os.path.abspath(__file__))
    csv_file = open(path + Config.file_path)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rows = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            polyline = row[8]
            polyline = polyline[1:-1]
            polyline = re.findall(r'\[(.+?)\]', polyline)
            taxi_locations_list = []
            for point in polyline:
                lat = float(point.split(",")[0])
                long = float(point.split(",")[1])
                taxi_location = Location(lat, long)
                taxi_locations_list.append(taxi_location)
            taxi_data = TaxiData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], taxi_locations_list)
            rows.append(taxi_data)
            line_count += 1
    return rows
