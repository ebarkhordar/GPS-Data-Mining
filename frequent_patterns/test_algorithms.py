from frequent_patterns.apriori import do_efficient_apriori
from frequent_patterns.eclat import do_eclat
from frequent_patterns.efficient_apriori import do_apriori
from frequent_patterns.fpgrowth import do_fp_growth

if __name__ == '__main__':
    transactions = []
    with open('data.text', 'r') as fh:
        for line in fh:
            numbers_list = line.split(" ")
            numbers_list.remove('\n')
            numbers_tuple = tuple(numbers_list)
            transactions.append(numbers_tuple)

    min_support = 0.06
    do_eclat(min_support)
    do_efficient_apriori(min_support)
    do_apriori(min_support)
    do_fp_growth(min_support)
