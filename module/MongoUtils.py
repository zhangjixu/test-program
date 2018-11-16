# -*- coding: utf-8 -*-

import pymongo


class MongoUtils(object):
    '''
    用于构建 mongo 操作类
    '''

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
        返回 mongo 的实例 并设置读取策略为 secondaryPreferred 优先读取副节点，失败则从主节点读取。
        Returns:

        '''
        client = pymongo.MongoClient(host=str(self._url), readPreference='secondaryPreferred')
        # 指定数据库
        db = client[self._database]
        collection = db[self._collection]
        return collection
