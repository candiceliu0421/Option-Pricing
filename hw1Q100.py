#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:31:50 2017

@author: candice
"""

array=[]
for i in range(0,1000000):   #open an array
    array.append(0)


while True:
    try:
        str=input()
        tmp=str.split()
        max=0
        if( int(tmp[0]) >int(tmp[1])):
          end=int(tmp[0])
          start=int(tmp[1])
        else:
          end=int(tmp[1])
          start=int(tmp[0])

    except EOFError:
        break
    

    for n in range(start,end+1):
        num=n
        
        count=1
        while(num!=1):       
          #print(n)
          if(num<1000000 and array[num]!=0): 
              count += array[num]    
              count-=1
              break
          elif(num%2 ==1):
              num = 3*num + 1
          else:  
              num = num//2
          count+=1
          
        if(array[n]==0):   
            array[n]=count
                    
        if(count > max):
            max = count
    
    if( int(tmp[0]) <int(tmp[1])):
        print(start,end,max)
    else:
        print(end,start,max)