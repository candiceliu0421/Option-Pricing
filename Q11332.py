#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:01:17 2017

@author: candice
"""


x=int(input())
while(x!=0):
    while(x>=10):
        y=0
        while(x>0):
            y=y+x%10
            x=x//10
        x=y
    print(x)
    x=int(input())