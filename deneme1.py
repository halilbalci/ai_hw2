#Halil Balcı 230201022
import numpy as np
import sys 
filename="data 1.npy"
nodes = np.load(filename)
totalLen=len(nodes[0])
calculated_p_before={}#calculated p's added to the dictionary. Dont calculate same variables again.

#P(a,b,c,d,e,f,g)=P(A)*P(B)*P(C|A)*P(D|A,B)*P(E|C)*P(F|C)*P(G|D)
#P(C|A)=p(C,A)/P(A)      P(E|C)=P(E,C)/P(C)     P(F|C)=P(F,C)/P(C)     P(G|D)=P(G,D)/P(D)
#P(D|A,B)=P(D,A,B)/P(A,B)

"""----------CALCULATE FROM DATA-----------------------------------------------------------------------------------------"""
def p(variables): #p("d,ng,a,c")
    dictKey=variables
    if(variables in calculated_p_before):# if variable calculated before, return it without calculation
        return calculated_p_before[variables]
    if("," not in variables):
        isNegativeVar=isStringStartWithN(variables) # nG => negativeVar true, G => negativeVar False
        if(isNegativeVar):
            variables=removeFirstletter(variables)
        index=lettersToNumber(variables)
        prob = sum(nodes[index])/totalLen
        if(isNegativeVar):
            calculated_p_before.update({dictKey:1-prob})
            return 1-prob
        calculated_p_before.update({dictKey:prob})
        return prob
    else:
        letterIndex=[]
        sign=[]
        variables=variables.split(",")
        for i in variables: # variables = example: A,nG  convert them to letterindex=>(a=0,b=1...g=6) and sign=>(a=True or na=False)
            if(isStringStartWithN(i)):
                i=removeFirstletter(i)
                sign.append(False)
            else:
                sign.append(True)
            letterIndex.append(lettersToNumber(i))
        counter=0
        for column in zip(*nodes):
            check=True # all variables in column(letterindex[x])==sign[x]
            for x in range(len(letterIndex)):
                if(not(column[letterIndex[x]]==sign[x])):
                    check=False
            if(check):
                counter+=1
        prob=counter/totalLen
        calculated_p_before.update({dictKey:prob}) # first time calculated variables added to the dictionary
        return prob
            
#a=0,b=1,c=2 ... given letter is converted to the index.
def lettersToNumber(letter):
    letter=letter.lower()
    return  ord(letter) - 97
def isStringStartWithN(string):
    return ("n" in string)
def removeFirstletter(string):
    return string[1:]
"""----------------------------------------------------------------------------------------------------------------------"""
def app():
    query=input("please give query variables:")
    if(query=="quit"):
        sys.exit()
    evidence=input("please give evidence variables:")
    denominator_string=evidence.lower().replace(" ",",")
    numerator_string=query.lower().replace(" ",",")+","+evidence.lower().replace(" ",",")
    print("The probability calculated from data is: ",p(numerator_string)/p(denominator_string))
    print("The probability calculated by inference is",calculateByInference(numerator_string,denominator_string))
    print("------------------------------------------------------------------")
def initializeDomains(string):
    #theList[0]=A domain, theList[1]=B domain
    theDomain=[["a","na"],["b","nb"],["c","nc"],["d","nd"],["e","ne"],["f","nf"],["g","ng"]]
    splitted_string=string.split(",")
    for var in splitted_string:
        if(isStringStartWithN(var)):
            var_without_n=removeFirstletter(var)
            index=lettersToNumber(var_without_n)
            if(var_without_n in theDomain[index]):
                theDomain[index].remove(var_without_n)
        else:
            index=lettersToNumber(var)
            if("n"+var in theDomain[index]):
                theDomain[index].remove("n"+var)
    return theDomain
"""----------CALCULATE BY INFERENCE--------------------------------------------------------------------------------------"""
def calculateByInference(numerator_string,denominator_string):
    return calculation(numerator_string)/calculation(denominator_string)
    
def calculation(string):
    result=0
    domain=initializeDomains(string)
    if([] in domain):
        return 0
    for a in domain[0]:
        for b in domain[1]:
            for c in domain[2]:
                for d in domain[3]:
                    for e in domain[4]:
                        for f in domain[5]:
                            for g in domain[6]:
                                result+=p(a)*p(b)*(p(c+","+a)/p(a))*(p(d+","+a+","+b)/p(a+","+b))*(p(e+","+c)/p(c))*(p(f+","+c)/p(c))*(p(g+","+d)/p(d))
                                #P(a,b,c,d,e,f,g)=P(A)*P(B)*P(C|A)*P(D|A,B)*P(E|C)*P(F|C)*P(G|D)
    return result
print("Program is initializing.\n Test case is calculating .Please wait.")
print("P(D,nG| A C);")
print("The probability calculated by inference is",calculateByInference("d,ng,a,c","a,c"))
print("The probability calculated from data is: ",p("d,ng,a,c")/p("a,c"))
loop=1
while loop:
    try:
        app()
    except SystemExit:
                print("Good bye")
                loop=0
    except:
        print("Wrong input Try again")
        