# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:45:58 2021

@author: Fen Lisesi
"""
t = int(input())
for t in range (0,t):
    a1,a2,a3,a4,a5,a6,a7 = map(int, input().split())
    sorta = [a1,a2,a3,a4,a5,a6,a7]
    sorta.sort()
    c = sorta[6]-(sorta[1]+sorta[0])
    print((sorta[0]),sorta[1],c)
    