from frequent_patterns.apriori import do_apriori
from frequent_patterns.eclat import do_eclat
from frequent_patterns.ef_apriori import do_efficient_apriori
from frequent_patterns.fpgrowth import do_fp_growth

if __name__ == '__main__':
    min_support = 0.05
    do_apriori(min_support)
    do_efficient_apriori(min_support)
    do_eclat(min_support)
    do_fp_growth(min_support)
