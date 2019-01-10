from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

from data_utils.data import return_data_rows
from data_utils.distance import calculate_distance


class Regression:
    def __init__(self):
        pass

    def find_sum(l, p):
        res = 0

        for i in l:
            res += i ** p

        return res

    def find_mul_sum(l1, l2):
        res = 0

        for i in range(len(l1)):
            res += (l1[i] * l2[i])

        return res

    def solve_equ(sum_x, sum_x2, sum_y, sum_xy):

        n = 30

        p = np.array([[sum_x, n], [sum_x2, sum_x]])
        q = np.array([sum_y, sum_xy])

        res = np.linalg.solve(p, q)

        return res

    def predict(x, res):
        y_pred = []

        for i in x:
            y_pred.append(res[0] * i + res[1])

        return y_pred


def main():
    result = return_data_rows()
    distance_list = []
    hour_and_min = []
    for row in result:
        polyline_locations = row.polyline
        for i in range(len(polyline_locations) - 1):
            distance = calculate_distance(polyline_locations[i], polyline_locations[i + 1])
            distance = distance * 1000
            distance_list.append(distance)
            trip_datetime = datetime.fromtimestamp(row.timestamp)
            hour_and_min.append(int(str(trip_datetime.hour)+str(trip_datetime.minute)))

    x = hour_and_min
    print(hour_and_min)
    y = distance_list

    r = Regression

    sum_x = r.find_sum(x, 1)
    sum_y = r.find_sum(y, 1)
    sum_x2 = r.find_sum(x, 2)
    sum_xy = r.find_mul_sum(x, y)

    res = []

    res = r.solve_equ(sum_x, sum_x2, sum_y, sum_xy)

    y_pred = r.predict(x, res)

    plt.scatter(x, y, color='red')
    plt.plot(x, y_pred, color='blue')
    plt.title('Distance per day time Regression')
    plt.xlabel('Time (from 00:00 to 24:00)')
    plt.ylabel('Distance')
    plt.show()


if __name__ == "__main__":
    main()
