import csv
import re

from csv.models import TaxiData

file_path = "Porto_taxi_data_test_partial_trajectories.csv"


def return_data_rows():
    csv_file = open(file_path)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rows = []
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {}'.format(", ".join(row)))
            line_count += 1
        else:
            polyline = row[8]
            polyline = polyline[1:-1]
            polyline = re.findall(r'\[(.+?)\]', polyline)
            taxi_data = TaxiData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], polyline)
            rows.append(taxi_data)
            line_count += 1
    print('Processed {} lines.'.format(line_count))
    return rows

