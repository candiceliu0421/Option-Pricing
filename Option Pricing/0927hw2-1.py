#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:59:39 2017

@author: candice
"""

import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def blscall(S,L,T,r,sigma):
    d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
    d2 = d1- sigma*math.sqrt(T)
    return S*norm.cdf(d1)-L*math.exp(-r*T)*norm.cdf(d2)

S = 50.0
L = 40.0
T = 2.0
r = 0.08
sigma = 0.2

print(blscall(S,L,T,r,sigma))
print(blscall(S,L,T,r,sigma)+L*math.exp(-r*T)-S)
d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
print(norm.cdf(d1))
print((blscall(S+0.01,L,T,r,sigma)-blscall(S-0.01,L,T,r,sigma))/0.02)

N = 100
dt = T/N

P = np.zeros([10000,N+1])
for i in range(10000):
    P[i,0]=S
    for j in range(N):
        P[i,j+1]=P[i,j]*math.exp((r-0.5*sigma*sigma)*dt+np.random.normal(0,1,1)*sigma*math.sqrt(dt))
        
C = 0
for i in range(10000):
    if(P[i,100]>L):
        C += (P[i,100]-L)/10000
print(C*math.exp(-r*T))

for i in range(200):
  x = []
  y = []
  for j in range(101):
      x.append(j)
      y.append(P[i,j])
      
  plt.plot(x,y)

plt.show()