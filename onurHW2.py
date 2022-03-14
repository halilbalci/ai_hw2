import numpy as np

def p(lettersSet):
    lettersSet = sorted(lettersSet)
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
    return p

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
        if("a" in l):
            A=["a"]
        if("na" in l):
            A=["na"]
        if("b" in l):
            B=["b"]
        if("nb" in l):
            B=["nb"]
        if("c" in l):
            B=["c"]
        if("nc" in l):
            C=["nc"]
        if("d" in l):
            D=["d"]
        if("nd" in l):
            D=["nd"]
        if("e" in l):
            E=["e"]
        if("ne" in l):
            E=["ne"]
        if("f" in l):
            F=["f"]
        if("nf" in l):
            F=["nf"]
        if("g" in l):
            G=["g"]
        if("ng" in l):
            G=["ng"]
            
    r=0
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    for e in E:
                        for f in F:
                            for g in G:
                                r+=p(set([a]))*p(set([b]))*(p(set([a,c]))/p(set([a])))*(p(set([a,b,d]))/p(set([a,b])))*(p(set([c,e]))/p(set([c])))*(p(set([c,f]))/p(set([c])))*(p(set([d,g]))/p(set([d])))
    return r
    
def main():
    query=input("please give query variables:")
    evidence=input("please give evidence variables:")
    splitted_query = query.lower().split()
    splitted_evidence = evidence.lower().split()
    evidenceSet = set(splitted_evidence)
    querySet=set(splitted_query)
    querySet=querySet.union(evidenceSet)
    print("by ınference=",byInference(querySet,evidenceSet))
    print("from data=",p(querySet)/p(evidenceSet))

filename="data 1.npy"
data = np.load(filename)
totalLen=len(data[0])
calculated_p={}
main()