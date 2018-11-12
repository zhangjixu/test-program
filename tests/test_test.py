# coding:utf-8

import time
import itertools
from utils import logger

DATETIME_FORMAT = '%Y-%m-%d'
log = logger.log


def str_json():
    string = '1314:英镑,1315:港币,1316:美元,1317:瑞士法郎,1318:德国马克,1319:法国法郎,1375:新加坡元,1320:瑞典克朗,1321:丹麦克朗,' \
             '1322:挪威克朗,1323:日元,1324:加拿大元,1325:澳大利亚元,1326:欧元,1327:澳门元,1328:菲律宾比索,1329:泰国铢,1330:新西兰元,' \
             '1331:韩元,1843:卢布,2890:林吉特,2895:新台币,1370:西班牙比塞塔,1371:意大利里拉,1372:荷兰盾,1373:比利时法郎,1374:芬兰马克,' \
             '3030:印尼卢比,3253:巴西里亚尔,3899:阿联酋迪拉姆,3900:印度卢比,3901:南非兰特,4418:沙特里亚尔,4560:土耳其里拉'
    list_str = string.split(',')
    dic = {}
    for str in list_str:
        arr = str.split(':')
        dic[arr[1]] = arr[0]

    for key, value in dic.iteritems():
        print key
        print value


def test_date(start_date):
    try:
        if not start_date:
            print ' ========== ' + start_date
            time.strptime(start_date, DATETIME_FORMAT)

        print start_date
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    # x = [1, 2, 7, 3]
    # y = ['a', 'b', 'e', 'd']
    # lists = sorted(itertools.izip(*[x, y]))
    # print lists
    # new_x, new_y = list(itertools.izip(*lists))
    # print list(itertools.izip(*lists))
    log.error('sss % s' % (9))
