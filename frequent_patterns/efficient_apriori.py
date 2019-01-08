from datetime import datetime
from apyori import load_transactions
from apyori import apriori


def do_apriori(min_support):
    with open('data.text') as f:
        transactions = load_transactions(f, delimiter=" ")
        start_time = datetime.now()
        item_sets = list(apriori(transactions, min_support=min_support, min_confidence=1))
        end_time = datetime.now()
        diff = (end_time - start_time)
        print(item_sets)
        print("apriori longs : ", diff.total_seconds(), "seconds")
