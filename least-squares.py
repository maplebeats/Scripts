#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
mv=x0+x1*g
https://zh.wikipedia.org/zh/最小二乘法

'''

mv = [int(i) for i in input("Please input mv:").split()]
g = [int(i) for i in input("Please input g").split()]

print((lambda mv,g:'mv='+str((lambda mv,g:sum(mv)/len(mv)-((lambda mv,g:sum([(i-sum(mv)/len(mv))*(j-sum(g)/len(g)) for i,j in zip(mv,g)])/sum([(i-sum(g)/len(g))**2 for i in g]))(mv,g))*(sum(mv)/len(mv)))(mv,g))+'+'+str(sum([(i-sum(mv)/len(mv))*(j-sum(g)/len(g)) for i,j in zip(mv,g)])/sum([(i-sum(g)/len(g))**2 for i in g]))+'*g')(mv,g))
