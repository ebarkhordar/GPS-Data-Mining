from datetime import datetime
from fim import eclat

from data_utils.data import return_data_rows


def do_eclat(min_support):
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
    rules = eclat(transactions, supp=min_support * 10)
    rules.sort(key=lambda x: x[1], reverse=True)
    end_time = datetime.now()
    print(rules)
    diff = (end_time - start_time)
    print("eclat longs : ", diff.total_seconds(), "seconds")
