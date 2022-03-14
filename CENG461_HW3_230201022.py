#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:57:34 2021

@author: halil
"""
import time
import matplotlib.pyplot as plt

def reward(s):
    if(s*1.25<M):
        a=s*0.25
    else:
        a=M-s
    if(s*1.5<M):
        b=s*0.5
    else:
        b=M-s
    if(s*1.75<M):
        c=s*0.75
    else:
        c=M-s
    expectedHarvest=0+0.3*a+0.3*b+0.2*c
    return expectedHarvest

def valueIteration():
    for i in range(M+1):
        dic={}
        for action in range(i+1):
            dic[action]=utilities[i-action]/(i+1) #P(s''|s,a)*u(s'')
        utilities[i]=reward(i)+gama*max(dic.values()) #U[i+1]=R(i)+gama*max(P(s'|s,a)*u(s'))
    
def policy():
    policy=[0]*(M+1)
    max_utility_index=utilities.index(max(utilities))#max utilities index
    for i in range(M+1):
        fishPop=i-max_utility_index
        if(fishPop >0):
            policy[i]=fishPop
        else:
            policy[i]=0
    return policy

valueIterStart=time.time()
gama=1
M=100

utilities=[0]*(M+1)
plt.plot(policy())
plt.title('all utilities are 0')
plt.ylabel('harvest')
plt.xlabel('fish population')
plt.show()
temp=utilities.copy()
for i in range(1000):
    valueIteration()
valueIterEnd=time.time()
plt.plot(policy())
plt.title('optimum policy for highest total harvest')
plt.ylabel('harvest')
plt.xlabel('fish population')
plt.show()
print("valueIteration takes ",valueIterEnd-valueIterStart,"second")
