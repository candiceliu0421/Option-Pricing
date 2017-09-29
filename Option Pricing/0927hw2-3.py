#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:06:53 2017

@author: candice
"""

import math
from scipy.stats import norm
import matplotlib.pyplot as plt

def blscall(S,L,T,r,sigma):
    d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
    d2 = d1- sigma*math.sqrt(T)
    return S*norm.cdf(d1)-L*math.exp(-r*T)*norm.cdf(d2)

def Bisection2(left,right,S,L,T,r,call,error,iteration):
    center = (left+right)/2
    list1.append(center)
    if(iteration==0):
      return center
    if((blscall(S,L,T,r,left)-call)*(blscall(S,L,T,r,center)-call)<0):
      return Bisection2(left,center,S,L,T,r,call,error,iteration-1)
    else:
      return Bisection2(center,right,S,L,T,r,call,error,iteration-1)

def Newton(initsigma,S,L,T,r,call,iteration):
    sigma = initsigma
    for i in range(iteration):
        list2.append(sigma)
        fx = blscall(S,L,T,r,sigma)-call
        fx2 = (blscall(S,L,T,r,sigma+0.00000001)-blscall(S,L,T,r,sigma-0.00000001))/0.00000002
        sigma = sigma - fx/fx2
    return sigma

list1 = []
list2 = []

S = 10326.68
L = 10300.0
T = 21.0/365
r = 0.01065
sigma = 0.10508

list1.append(Bisection2(0.00000001,1,S,L,T,r,121.0,0.00000001,20))
list2.append(Newton(0.5,S,L,T,r,121.0,20))

plt.plot(list1)
plt.plot(list2)

plt.show()





"""
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
drawC = np.zeros([1,100])
for i in range(10000):
    if(P[i,100]>L):
        C += (P[i,100]-L)
    if(i%100==99):
        drawC[(i+1)//100-1]=C/(i+1)*math.exp(-r*T)-blscall(S,L,T,r,sigma)
        
print(C*math.exp(-r*T))"""