"""A helper script for wrapping database connection."""
import pymysql
from pymongo import MongoClient


def connectMongo(host='localhost'):
    """A helper for connecting Mongo."""
    client = MongoClient(host, 27017)
    return client


def connectMysql(host='localhost', user='wkp', passwd='',
                 db='wiki', use_unicode=True, charset='utf8'):
    """Connection to database."""
    db = pymysql.connect(host='localhost', user='wkp', passwd='',
                         db='wiki', use_unicode=True, charset='utf8')
    return db
