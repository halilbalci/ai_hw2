import numpy as np
filename="data 1.npy"
data = np.load(filename)
totalLen=len(data[0])
calculated_p={}

def p(lettersSet):
    str=""
    for l in lettersSet:
        str+=l
    
    if(str in calculated_p):
        return calculated_p[str]
    
    counter=0
    for i in range(totalLen):
        column = [row[i] for row in data]
        flag=True
        for letter in lettersSet:
            if("n" in letter):
                index = ord(letter[1]) - 97
                if(column[index]==True):
                    flag=False
            else:
                index = ord(letter) - 97
                if(column[index]==False):
                    flag=False
        if(flag):
            counter+=1
    p=counter/totalLen
    calculated_p.update({str:p})
    return counter/totalLen

def byInference(querySet,evidenceSet):
    if("a" in querySet and "na" in querySet):
        return 0
    if("b" in querySet and "nb" in querySet):
        return 0
    if("c" in querySet and "nc" in querySet):
        return 0
    if("d" in querySet and "nd" in querySet):
        return 0
    if("e" in querySet and "ne" in querySet):
        return 0
    if("f" in querySet and "nf" in querySet):
        return 0
    if("g" in querySet and "ng" in querySet):
        return 0
    print(querySet)
    print(evidenceSet)
    return calculate(querySet)/calculate(evidenceSet)
def calculate(lettersSet):
    A=["a","na"]
    B=["b","nb"]
    C=["c","nc"]
    D=["d","nd"]
    E=["e","ne"]
    F=["f","nf"]
    G=["g","ng"]
    for l in lettersSet:
        if("a" == l):
            A=["a"]
        elif("na" == l):
            A=["na"]
        elif("b" == l):
            B=["b"]
        elif("nb" == l):
            B=["nb"]
        elif("c" == l):
            C=["c"]
        elif("nc" == l):
            C=["nc"]
        elif("d" == l):
            D=["d"]
        elif("nd" == l):
            D=["nd"]
        elif("e" == l):
            E=["e"]
        elif("ne" == l):
            E=["ne"]
        elif("f" == l):
            F=["f"]
        elif("nf" == l):
            F=["nf"]
        elif("g" == l):
            G=["g"]
        elif("ng" == l):
            G=["ng"]
    
            
    r=0
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    for e in E:
                        for f in F:
                            for g in G:
                                print(a,b,c,d,e,f,g)
                                r+=p(set([a]))*p(set([b]))*(p(set([a,c]))/p(set([a])))*(p(set([a,b,d]))/p(set([a,b])))*(p(set([c,e]))/p(set([c])))*(p(set([c,f]))/p(set([c])))*(p(set([d,g]))/p(set([d])))
                                print("r=",r)
    return r
    
def app():
    querySet=set()
    evidenceSet=set()
    query=input("please give query variables:")
    evidence=input("please give evidence variables:")
    splitted_query= query.lower().split()
    splitted_evidence = evidence.lower().split()
    for x in splitted_query:
        querySet.add(x)
    for y in splitted_evidence:
        querySet.add(y)
        evidenceSet.add(y)
    
    print("from data=",p(querySet)/p(evidenceSet))
    print("by ınference=",byInference(querySet,evidenceSet))


app()