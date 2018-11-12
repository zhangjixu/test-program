# coding:utf-8

from conf import mongo_conf
import pymongo

client = pymongo.MongoClient(host=mongo_conf.ip, port=mongo_conf.port)
# 指定 db
db = client['test']


def query():
    collection = db.use
    doc = {'age': 18}
    collection.insert(doc)
    print 'success'


if __name__ == '__main__':
    query()
