# pcost.py
#
# Exercise 1.27

import sys
def portfolio_cost(filename):
    'Adds up the cost/value of shares in a portfolio when passed a properly formatted csv file'
    
    import csv
     
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            #row = line.split(',')
            #print(row)
            try:
                 total_cost = total_cost + (int(line[1]) * float(line[2]))
            except ValueError:
                print("Couldn't parse", line)


    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost ${cost:0.2f}')