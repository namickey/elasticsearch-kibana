# encoding: utf-8

from datetime import datetime
from elasticsearch import Elasticsearch
import pandas as pd

def hoge():
    es = Elasticsearch()
    doc = {
        'author': 'aaa',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="hoge", id=5, body=doc)
    print(res['result'])

def up():
    df = pd.read_csv('up.csv')
    print(df)
    df = df.T
    print(df)
    es = Elasticsearch()
    i = 0
    for col in df:
        year = 0
        for index, row in zip(df[col].index, df[col]):
            if year == 0:
                print('***')
                year = row
            else:
                print(str(datetime(year, int(index), 1)) + ':' + str(row))
                i += 1
                regist(es, i, datetime(year, int(index), 1), row)

def regist(es, count, date, up):
    doc = {
        'timestamp': date,
        'up': up,
    }
    res = es.index(index="up", id=count, body=doc)
    print(res['result'])
up()
#hoge()
