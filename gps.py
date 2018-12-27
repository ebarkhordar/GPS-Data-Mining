import csv
import pyfpgrowth

if __name__ == '__main__':
    with open('taxi_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        transactions = []
        for row in csv_reader:
            if line_count == 0:
                print('Column names are {}'.format(row))
                line_count += 1
            else:
                polyline = row[8]
                polyline = polyline[1:-1]
                polyline = polyline.split('], [')
                polyline_list = set()
                for point in polyline:
                    lat = point.split(", ")[0]
                    lat = lat.replace("[", "")
                    long = point.split(", ")[1]
                    long = long.replace("[", "")
                    lat = lat[:7]
                    long = long[:6]
                    new_point = str(lat + "," + long)
                    polyline_list.add(new_point)
                transactions.append(polyline_list)
                line_count += 1
        patterns = pyfpgrowth.find_frequent_patterns(transactions, 10)
        print("patterns", patterns)
