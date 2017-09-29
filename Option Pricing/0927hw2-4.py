#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:39:20 2017

@author: candice
"""
import math
from scipy.stats import norm
import matplotlib.pyplot as plt

def blscall(S,L,T,r,sigma):
    d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    return S*norm.cdf(d1)-L*math.exp(-r*T)*norm.cdf(d2)

def Newton(initsigma,S,L,T,r,call,iteration):
    sigma = initsigma
    for i in range(iteration):
        fx = blscall(S,L,T,r,sigma)-call
        fx2 = (blscall(S,L,T,r,sigma+0.00000001)-blscall(S,L,T,r,sigma-0.00000001))/0.00000002
        sigma = sigma -fx/fx2
    return sigma

list = []

S = 10326.68
L = 10300.0
T = 21.0/365
r = 0.01065
sigma = 0.10501

L = 10000.0
list.append(Newton(0.5,S,L,T,r,354.0,20))

L = 10100.0
list.append(Newton(0.5,S,L,T,r,267.0,20))

L = 10200.0
list.append(Newton(0.5,S,L,T,r,187.0,20))

L = 10300.0
list.append(Newton(0.5,S,L,T,r,121.0,20))

L = 10400.0
list.append(Newton(0.5,S,L,T,r,69.0,20))

L = 10500.0
list.append(Newton(0.5,S,L,T,r,34.0,20))

L = 10600.0
list.append(Newton(0.5,S,L,T,r,14.5,20))

L = 10700.0
list.append(Newton(0.5,S,L,T,r,5.80,20))

plt.plot(list)
plt.show()