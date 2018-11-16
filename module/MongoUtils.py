# -*- coding: utf-8 -*-

import pymongo


class MongoUtils(object):
    '''
    用于构建 mongo 操作类
    '''
    db_client = {}
    collection_client = {}

    def __init__(self, url, database, collection):
        '''
        初始化参数
        Args:
            url:
            database:
            collection:
        '''
        self._url = 'mongodb://' + url
        self._database = database
        self._collection = collection

    def getMongo(self):
        '''
        返回 mongo 的实例，并设置读取策略为 secondaryPreferred (优先读取副节点，失败则从主节点读取)。
        Returns:

        '''
        client = pymongo.MongoClient(host=str(self._url), readPreference='secondaryPreferred')
        db_key = str(self._url) + str(self._database)
        # 指定数据库
        if db_key not in self.db_client:
            db = client[self._database]
            self.db_client[db_key] = db
        else:
            db = self.db_client[db_key]

        collection_key = db_key + str(self._collection)
        # 指定 collection
        if collection_key not in self.collection_client:
            collection = db[self._collection]
            self.collection_client[collection_key] = collection
        else:
            collection = self.collection_client[collection_key]

        return collection
