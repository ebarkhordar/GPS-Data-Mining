from datetime import datetime
from efficient_apriori import apriori


def do_efficient_apriori(min_support):
    transactions = []
    with open('data.text', 'r') as fh:
        for line in fh:
            numbers_list = line.split(" ")
            numbers_list.remove('\n')
            numbers_tuple = tuple(numbers_list)
            transactions.append(numbers_tuple)
    start_time = datetime.now()
    item_sets = apriori(transactions, min_support=min_support, min_confidence=1)
    end_time = datetime.now()
    diff = (end_time - start_time)
    print(item_sets)
    print("efficient apriori longs : ", diff.total_seconds(), "seconds")
