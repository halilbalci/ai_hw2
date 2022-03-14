#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:17:45 2021

@author: halil
"""
M=101
Ui=[0]*M
gama=0.9
import random
def R(s):
    if (s==0):#overkill
        return -100
    return s
def initializeU0():
    for i in range(M):
        Ui[i]=R(i)
def maximize(state):
    dic={}
    actions=list(range(state+1))
    actionsNumber=len(actions)+1
    for action in actions:
        nextState=state-action
        dic[action]=gama*Ui[nextYearExpectedFishPop(nextState)] #gama * max P(s'|s,a)*u(s')
        #dic[action]=gama*Ui[nextYearExpectedFishPop(nextState)]/actionsNumber
    max_value = max(dic.values())
    for k,v in dic.items():
        if(v==max_value):
            max_action=k
    return state-max_action,state,max_action,max_value #nextState,state,action,best action value

def updateUi():
    for i in range(M):#0-100
        Ui[i]+=maximize(i)[3]+R(i)
        
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
    if(x>M-1):
        return M-1
    return round(x)
initializeU0()
counter=100
currentFish=80
totalHarvest=0

while(counter>0):
    counter-=1
    u=maximize(currentFish) #nextState,state,action,best action value
    currentFish=u[0]
    totalHarvest+=u[2]
    updateUi()
    if(counter!=0):
        currentFish=aYearPassed(currentFish)
print("currentFish=",currentFish)
print("totalHarvest=",totalHarvest)
