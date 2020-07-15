# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    'Reads portfolio file into a list of tuples'
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            line = (row[0], int(row[1]), float(row[2]))
            portfolio.append(line)

    return portfolio

