# -*- coding: utf-8 -*-

import re


def test_re():
    pattern_1 = '(var m_nRecordCount = )'
    p = re.compile(pattern_1)
    str_1 = p.sub('', '''www 
        var m_nRecordCount = 56695;
        var m_nPageSize = 20;
        aa''')
    str = p.sub('', str_1)

    pattern_2 = '(;)'
    p = re.compile(pattern_2)
    str = p.sub('', str)
    print str


def test_re_1():
    pattern = '\n'
    p = re.compile(pattern)
    str_1 = p.sub('', '''www 
    var m_nRecordCount = 56695;
    var m_nPageSize = 20;
    aa''')
    str = p.sub('', str_1)
    print str


if __name__ == '__main__':
    test_re()
