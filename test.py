# from pyfpgrowth import pyfpgrowth
#
# transactions = [['1', '2', '5'],
#                 ['1', '2', '3', '5'],
#                 ['1', '2', '3']]
#
# patterns = pyfpgrowth.find_frequent_patterns(transactions, 3)
# print("patterns", patterns)
#
#
#
import re

test_polyline = "[[-8.585676, 41.148522], [-8.585712000000001, 41.148638999999996], [-8.586999, 41.147459999999995]]"
m = re.findall(r'\[(.+?)\]', test_polyline)
if m:
    print(m)
