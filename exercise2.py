# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:29:40 2024

@author: s_willrich20
"""
def teilen(x,y):
    if y==0 :
        print("Es ist nicht möglich durch 0 zu teilen")
    elif x==y:
        print ("x=y")
    else:
        if x % y ==0:
            print(x/y)
        else:
            print("Das ist nicht schön teilbar")
        