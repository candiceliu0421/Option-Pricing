#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:38:42 2017

@author: candice
"""

for case in range(1, 1 + int(input())):
    s = input()
    res = []
    currC = ''
    count = 0
    for c in s:
        if c in set('0123456789'): 
            count *= 10
            count +=int(c)
        else:
            res.append(currC * count)
            currC = c
            count=0
    res.append(currC * count)
    print('Case %d: %s' % (case, ''.join(res)))