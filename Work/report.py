# report.py
# -*- coding: utf-8 -*-
import csv

def read_portfolio(filename):
    portfolio = []
    holding = {}
    sum = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            name = record['name']
            nshares = int(record['shares'])
            price = float(record['price'])
            holding = {
                'name' :  record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
          
            portfolio.append(holding)
            sum += nshares  * price    
    
    return portfolio

def read_prices(filename):
     import csv

     f = open(filename, 'r')
     rows = csv.reader(f)
     stock = {}
     for row in rows:
        try:
            stock[row[0]] = float(row[1])
        except:
            pass
     f.close()

     return stock

#portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
prices    = read_prices('Data/prices.csv')
# �̷��� �̸� �־�θ� �˾Ƽ� ���� ����Ǿ�����(�͹̳ο��� ���� ���� ���ص�)

def cal_profit(portfolio, price):
    sum = 0
    for stock in portfolio[0]:
        if stock['name'] in prices.keys(): 
# �̷��� if�� ���� �ʿ���� stock���� price ��ųʸ����� �˻��ϴ� �Ŵϱ�
            sum += stock['shares'] * float(prices[stock['name']])
        else:
            pass
    return sum 

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        name = s['name']
        share = s['shares']
        price_b = s['price']
        price = float(prices[s['name']])
        report.append((name, share, price, price-price_b))
    return report

report = make_report(portfolio, prices)

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for name, shares, price, change in report:
         print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolio_file, prices_flie):
    portfolio = read_portfolio(portfolio_file)
    prices   = read_prices(prices_flie)
    report = make_report(portfolio, prices)
    print_report(report)


# Exercise 2.4
