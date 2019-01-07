import matplotlib.pyplot as plt
from data_utils.data import return_data_rows
from main_config import Config


def draw_origin_paths():
    rows = return_data_rows()
    for data in rows:
        one_taxi_polyline = data.polyline
        points_list = []
        for point in one_taxi_polyline:
            points_list.append([point.lat, point.long])
        plt.plot(*zip(*points_list), linewidth=0.5)
        plt.title("Raw-paths")
    # and finally save it with high resolution
    plt.savefig(Config.assets_path + 'origin-paths.png', dpi=500)



def draw_origin_paths():
    rows = return_data_rows()
    for data in rows:
        one_taxi_polyline = data.polyline
        points_list = []
        for point in one_taxi_polyline:
            points_list.append([point.lat, point.long])
        plt.plot(*zip(*points_list), linewidth=0.5)
        plt.title("Raw-paths")
    # and finally save it with high resolution
    plt.savefig(Config.assets_path + 'origin-paths.png', dpi=500)


if __name__ == '__main__':
    draw_origin_paths()
    plt.show()
