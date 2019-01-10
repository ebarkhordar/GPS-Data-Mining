from datetime import datetime
from efficient_apriori import apriori
from data_utils.data import return_data_rows


def do_efficient_apriori(min_support):
    transactions = []
    result = return_data_rows()
    for row in result:
        one_trip_locations = []
        for location in row.polyline:
            x = str(location.lat)[:8] + "," + str(location.long)[:8]
            one_trip_locations.append(x)
        numbers_tuple = tuple(one_trip_locations)
        transactions.append(numbers_tuple)
    start_time = datetime.now()
    item_sets = apriori(transactions, min_support=min_support/10, min_confidence=1)
    end_time = datetime.now()
    diff = (end_time - start_time)
    print(item_sets)
    print("efficient apriori longs : ", diff.total_seconds(), "seconds")

