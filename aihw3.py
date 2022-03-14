import random
def R(state,nextState):
    return state-nextState
def U(state,actions):
    lamda=0.9
    values=[]
    nextStateValues=[]
    for nextState in actions:
        values.append(lamda*nextYearExpectedFishPop(nextState) + R(state,nextState))
        nextStateValues.append(nextState)
        #print(state,"---",nextState,"-----",nextYearFishExpectedFishPop(nextState) + R(state,nextState) )
    #print("nextValue=" ,nextStateValues[values.index(max(values))])
    return nextStateValues[values.index(max(values))]
def nextYearExpectedFishPop(nextState):
    capacity=100
    a1=0.2*nextState
    a2=0.3*1.25*nextState
    a3=0.3*1.5*nextState
    a4=0.3*1.75*nextState
    pop=a1+a2+a3+a4
    pop=round(pop)
    if(pop>capacity): pop=capacity
    return pop
    
    #return max([0.2*(state-nextState)+0.3*1.25*(state-nextState)+0.3*1.5*(state-nextState)+0.3*1.75*(state-nextState) + R(state,nextState) for nextState in actions])   
def actions(state):
    return list(range(state+1))
def growRateCalc():
    growRate=random.random()
    if(growRate < 0.2):
        growRate=1
    elif (growRate < 0.5):
        growRate=1.25
    elif (growRate < 0.8):
        growRate=1.5
    else:
        growRate=1.75
    return growRate
balık=60
total_harvest=0
for x in range(1000):
    kalanBalık=U(balık,actions(balık))
    harvest=balık-kalanBalık
    print(x,". yıl balık=",balık,"----harvest=",harvest,"-------kalanBalık=",kalanBalık)
    growRate=growRateCalc()
    balık=round(kalanBalık*growRate)
    total_harvest+=harvest
print("total_harvest=",total_harvest)