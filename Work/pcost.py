# pcost.py
# -*- coding: utf-8 -*-
import csv
import sys

def portfolio_cost(path):
    total_cost = 0
    with open(path,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows,start=1):
            record = dict(zip(headers, row))
            print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares* price 
                """ 
                res += int(row[1]) * float(row[2])
                print(int(row[1]),float(row[2]),int(row[1]) * float(row[2]), total_cost)
                """
            except:
                 print(f'Row {rowno}: Bad row: {row}')
            """
            내가 했던 부분 
            headers = next(f)
            for line in f:
                row = line.split(',')
                res += int(row[1]) * float(row[2][:-1])
                print(int(row[1]),float(row[2][:-1]),int(row[1]) * float(row[2][:-1]), res)
            """
    return total_cost 

if len(sys.argv) ==2: # 
    filename = sys.argv[1] # sys.argv, 즉 인자값이 리스트형태로 길이 2 가질 때
    # 예시에서는 python3 pcost.py Data/portfolio.csv 의 pcost.py Data/portfolio.csv 부분 말함
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
#cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
#print(sys.argv[1])
    
# Exercise 1.27

