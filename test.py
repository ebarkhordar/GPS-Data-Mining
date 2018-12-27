from pyfpgrowth import pyfpgrowth

transactions = [['1', '2', '5'],
                ['1', '2', '3', '5'],
                ['1', '2', '3']]

patterns = pyfpgrowth.find_frequent_patterns(transactions, 3)
print("patterns", patterns)
