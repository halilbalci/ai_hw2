#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:47:57 2021

@author: halil
"""
import random
#R(s) + gama * max P(s'|s,a)*u(s')
gama=0.4
M=101 #0-100
policy=[0]*M
Ui=[0]*M
def aYearPassed(fish):
    r=random.random()
    if(r<0.2):
        fish*=1
    elif(r<0.5):
        fish*=1.25
    elif(r<0.8):
        fish*=1.5
    else:
        fish*=1.75
    if(round(fish)>100):
        return 100
    return round(fish)
def nextYearExpectedFishPop(state):
    x= 0.2*state + 0.3*1.25*state + 0.3*1.5*state + 0.2*1.75*state
    return round(x)
def nextYearExpectedFishPopWithCapacity(state):
    x= 0.2*state + 0.3*1.25*state + 0.3*1.5*state + 0.2*1.75*state
    if(x>M-1):
        return M-1
    return round(x)

def findPolicy(s):
    dic={}
    for action in range(s+1):
        dic[action]=R(s-action)+action
    max_value = max(dic.values())
    for k,v in dic.items():
        if(v==max_value):
            max_action=k
    policy[s]=s-max_action 
    return s-max_action #optimum nextState
def R(s):
    if(s==0):
        return -100
    if(nextYearExpectedFishPop(s)>=M):
        return M-(nextYearExpectedFishPop(s)-M)
    return s
def utility(s):
    #R(s) + gama * max P(s'|s,a)*u(s')
    nextState=findPolicy(s)
    Ui[s]=R(s)+gama*max([0.2*Ui[nextState],0.3*1.25*Ui[nextState],0.3*1.5*Ui[nextState],0.2*1.75*Ui[nextState]])
    return Ui[s]
fish=80
print("nextYearFish=",nextYearExpectedFishPop(fish))
print("R=",R(fish))
print("u",utility(fish))
print("policy=",policy[fish])
def Uiplus1():
    for i in range(101):
        utility(i)
for x in range(3):
    Uiplus1()
    fish=policy[fish]
    fish=nextYearExpectedFishPopWithCapacity(fish)
    print("nextYearExpectedFish=",nextYearExpectedFishPop(fish))
    print("R=",R(fish))
    print("u",utility(fish))
    print("policy=",policy[fish])