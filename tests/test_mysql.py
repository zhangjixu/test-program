# -*- coding: utf-8 -*-

from module.OpsMysql import OpsMysql


def query():
    ops_mysql = OpsMysql()
    sql = '''select * from test where id = %s and  name = %s '''
    data = ops_mysql.query(sql, ('17', u'李四'))
    for row in data:
        print(row)


def update():
    ops_mysql = OpsMysql()
    sql = '''insert into `test`(`name`, `age`) values(%s, %s)'''
    ops_mysql.update(sql, (u'王五', 19))
    print 'update success'


def insert_many():
    ops_mysql = OpsMysql()
    sql = '''insert into `test`(`name`, `age`) values(%s, %s)'''
    ops_mysql.inset_many(sql, [('ss', 19), ('dd', 20)])
    print 'insert_many success'


if __name__ == '__main__':
    insert_many()
