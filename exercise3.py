# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:53:46 2024

@author: s_willrich20
"""

def steigen(liste):
    x1= liste [0]
    x2= liste[1]
    y1= liste [2]
    y2= liste [3]
    
    dx= x2-x1
    dy= y2-y1
    
    if x1==x2:
        print("das geht so nicht")
    else:
        print (dy/dx)