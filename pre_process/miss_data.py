from data_utils.data import return_data_rows
from data_utils.distance import calculate_distance
import numpy as np
import operator
import matplotlib.pyplot as plt


def check_jump_data():
    result = return_data_rows()
    miss_data = []
    long_trip_dict = {}
    all_distance = []
    for row in result:
        polyline_locations = row.polyline
        for i in range(len(polyline_locations) - 1):
            distance = calculate_distance(polyline_locations[i], polyline_locations[i + 1])
            distance = distance * 1000
            all_distance.append(distance)
            if distance > 417:
                miss_data.append((row.trip_id, distance))
                if row.trip_id in long_trip_dict:
                    long_trip_dict[row.trip_id] = long_trip_dict[row.trip_id] + 1
                else:
                    long_trip_dict[row.trip_id] = 1

    sorted_long_trip_dict = sorted(long_trip_dict.items(), key=operator.itemgetter(1))
    from pylab import rcParams
    rcParams['figure.figsize'] = 20, 5
    key_list = []
    value_list = []
    for i in sorted_long_trip_dict:
        key_list.append(i[0])
        value_list.append(i[1])
    objects = tuple(key_list)
    y_pos = np.arange(len(objects))
    performance = value_list
    plt.bar(y_pos, performance, align='center', alpha=0.5, linewidth=0.5)
    plt.xticks(y_pos)
    plt.ylabel('Count of long distance')
    plt.xlabel('Trip ID')
    plt.title('long Distance between two locations')
    plt.savefig('long_distance.png', dpi=500)
    plt.show()


if __name__ == '__main__':
    check_jump_data()
