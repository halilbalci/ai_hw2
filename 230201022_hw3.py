#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:06:36 2021

@author: halil
"""
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


def nextYear(s):
    if(s*1.25<M):
        a=s*1.25
    else:
        a=M
    if(s*1.5<M):
        b=s*1.5
    else:
        b=M
    if(s*1.75<M):
        c=s*1.75
    else:
        c=M
    return s,round(a),round(b),round(c)
def valueIteration():
    for i in range(M+1):
        dic={}
        for action in range(i+1):
            p1,p2,p3,p4=nextYear(action)
            dic[action]=0.25*(utilities[p1]+utilities[p2]+utilities[p3]+utilities[p4]) #P(s''|s,a)*u(s'') !değiştirildi
        utilities[i]=reward(i)+gama*max(dic.values()) #U[i+1]=R(i)+gama*max(P(s''|s,a)*u(s''))
        
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
        
gama=0.9
M=100
utilities=[0]*(M+1)

plt.plot(policy())
plt.ylabel('harvest')
plt.show()
temp=utilities.copy()
for i in range(1000):
    valueIteration()
plt.plot(policy())
plt.ylabel('harvest after 100 valeue iteration')
plt.show()
