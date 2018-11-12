# coding:utf-8

from module.OpsMysql import OpsMysql

if __name__ == '__main__':
    ops_mysql = OpsMysql()
    sql = 'select * from test limit 5;'
    data = ops_mysql.query(sql)
    for row in data:
        print(row)
