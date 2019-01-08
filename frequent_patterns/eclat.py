from datetime import datetime
from fim import eclat


def do_eclat(min_support):
    transactions = []
    with open('data.text', 'r') as fh:
        for line in fh:
            numbers_list = line.split(" ")
            numbers_list.remove('\n')
            numbers_tuple = tuple(numbers_list)
            transactions.append(numbers_tuple)
    start_time = datetime.now()
    rules = eclat(transactions, supp=min_support * 100)
    rules.sort(key=lambda x: x[1], reverse=True)
    end_time = datetime.now()
    print(rules)
    diff = (end_time - start_time)
    print("eclat longs : ", diff.total_seconds(), "seconds")
