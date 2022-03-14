#Halil Balcı 230201002
import sys
import copy

#there are 10 types of constraint. Constraints are checking via isConstraintViolated(). if isConstraintViolated() is true, the given domain is not the solution. 
class Constraints_Type1: #if x=a then y=b
    def __init__(self,var1=None,var2=None,val1=None,val2=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
    #the function reassigns var1,val1,var2,var3 according to line
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 4 ):
            print("constraint type is not fit")
            return None
        try:
            self.var1= splitted_line[1].split("=")[0]
            self.val1=splitted_line[1].split("=")[1]
            
            self.var2= splitted_line[3].split("=")[0]
            self.val2=splitted_line[3].split("=")[1]
        except:
            print("line is not fit type1 constraints")
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            #print("indexOfVal1=",indexOfVal1)
            #print("indexOfVal2=",indexOfVal2)
            return (indexOfVal1%4 != indexOfVal2%4)
        except:
            return False
class Constraints_Type2: #if x=a then not y=b
    def __init__(self,var1=None,var2=None,val1=None,val2=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2    
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 5 ):
            print("constraint type is not fit")
            return None
        try:
            self.var1= splitted_line[1].split("=")[0]
            self.val1=splitted_line[1].split("=")[1]
            
            self.var2= splitted_line[4].split("=")[0]
            self.val2=splitted_line[4].split("=")[1]
        except:
            print("line is not fit type2 constraints")
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            return (indexOfVal1%4 == indexOfVal2%4)
        except:
            return False
class Constraints_Type3: #if x=a then either y=b or z=c
    def __init__(self,var1=None,var2=None,val1=None,val2=None,var3=None,val3=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.var3=var3
        self.val3=val3
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 7 ):
            print("constraint type is not fit")
            return None
        try:
            self.var1= splitted_line[1].split("=")[0]
            self.val1=splitted_line[1].split("=")[1]
            
            self.var2= splitted_line[4].split("=")[0]
            self.val2=splitted_line[4].split("=")[1]
            
            self.var3= splitted_line[6].split("=")[0]
            self.val3=splitted_line[6].split("=")[1]
        except:
            print("line is not fit type 3 constraints")
    def isConstraintViolated(self,domain,dataDict):
        isViolated=True
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            indexOfVal3=domain.index([self.val3])
        except:
            return False
        
        if((indexOfVal1%4 == indexOfVal2%4) or (indexOfVal1%4 == indexOfVal3%4)):
            isViolated = False
        if(indexOfVal1%4 == indexOfVal2%4):
            if(indexOfVal2%4 == indexOfVal3%4):
                return True
        return isViolated
class Constraints_Type4: #n(x=a) = n(y=b)
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 3 ):
            print("constraint type is not fit")
            return None
        try:
            first_func,last_func = splitted_line[0],splitted_line[2]
            temp=first_func.split("(")
            self.func=temp[0]
            temp =temp[1].split("=")
            self.var1=temp[0]
            self.val1=temp[1].split(")")[0]
            
            temp=last_func.split("(")
            if(temp[0]!= self.func):
                print("first and last functions are different")
                return None
            temp =temp[1].split("=")
            self.var2=temp[0]
            self.val2=temp[1].split(")")[0]
        except:
            print("line is not fit type 4 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])

        except:
            return False
        return not(indexOfVal1%4==indexOfVal2%4)
class Constraints_Type5: #n(x=a) = n(y=b) + m
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None,n=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
        self.n=n #string
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 5 ):
            print("constraint type is not fit")
            return None
        try:
            first_func,last_func,self.n = splitted_line[0],splitted_line[2],splitted_line[4]#n is assigned string
            temp=first_func.split("(")
            self.func=temp[0]
            temp =temp[1].split("=")
            self.var1=temp[0]
            self.val1=temp[1].split(")")[0]
            
            temp=last_func.split("(")
            if(temp[0]!= self.func):
                print("first and last functions are different")
                return None
            temp =temp[1].split("=")
            self.var2=temp[0]
            self.val2=temp[1].split(")")[0]

        except:
            print("line is not fit type 5 constraints")
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
        except:
            return False
        variables= list(dataDict.keys())
        x=variables.index(self.func)
        
        if((len(domain[4*x+(indexOfVal1%4)])==1) and (len(domain[4*x+(indexOfVal2%4)])==1)):
            a=int(domain[4*x+(indexOfVal1%4)][0])
            b=int(domain[4*x+(indexOfVal2%4)][0])
            return not (a  == (b + int(self.n)))
        
        return False
class Constraints_Type6: #n(x=a) = n(y=b) - m
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None,n=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
        self.n=n #string

    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 5 ):
            print("constraint type is not fit")
            return None
        try:
            first_func,last_func,self.n = splitted_line[0],splitted_line[2],splitted_line[4]#n is assigned string
            temp=first_func.split("(")
            self.func=temp[0]
            temp =temp[1].split("=")
            self.var1=temp[0]
            self.val1=temp[1].split(")")[0]
            
            temp=last_func.split("(")
            if(temp[0]!= self.func):
                print("first and last functions are different")
                return None
            temp =temp[1].split("=")
            self.var2=temp[0]
            self.val2=temp[1].split(")")[0]

        except:
            print("line is not fit type 5 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            #print("indexOfVal1=",indexOfVal1)
            #print("indexOfVal2=",indexOfVal2)
        except:
            return False
        variables= list(dataDict.keys())
        x=variables.index(self.func)
        
        if((len(domain[4*x+(indexOfVal1%4)])==1) and (len(domain[4*x+(indexOfVal2%4)])==1)):
            a=int(domain[4*x+(indexOfVal1%4)][0])
            b=int(domain[4*x+(indexOfVal2%4)][0])
            return not (a  == (b - int(self.n)))
        
        return False
class Constraints_Type7: #n(x=a) > n(y=b)
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 3 ):
            print("constraint type is not fit")
            return None
        try:
            first_func,last_func = splitted_line[0],splitted_line[2]
            temp=first_func.split("(")
            self.func=temp[0]
            temp =temp[1].split("=")
            self.var1=temp[0]
            self.val1=temp[1].split(")")[0]
            
            temp=last_func.split("(")
            if(temp[0]!= self.func):
                print("first and last functions are different")
                return None
            temp =temp[1].split("=")
            self.var2=temp[0]
            self.val2=temp[1].split(")")[0]
        except:
            print("line is not fit type 4 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])

        except:
            return False
        variables= list(dataDict.keys())
        x=variables.index(self.func)
        
        if((len(domain[4*x+(indexOfVal1%4)])==1) and (len(domain[4*x+(indexOfVal2%4)])==1)):
            a=int(domain[4*x+(indexOfVal1%4)][0])
            b=int(domain[4*x+(indexOfVal2%4)][0])
            return not (a  > b) 
        
        return False
class Constraints_Type8: #n(x=a) < n(y=b)
    def __init__(self,var1=None,var2=None,val1=None,val2=None,func=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.func=func
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 3 ):
            print("constraint type is not fit")
            return None
        try:
            first_func,last_func = splitted_line[0],splitted_line[2]
            temp=first_func.split("(")
            self.func=temp[0]
            temp =temp[1].split("=")
            self.var1=temp[0]
            self.val1=temp[1].split(")")[0]
            
            temp=last_func.split("(")
            if(temp[0]!= self.func):
                print("first and last functions are different")
                return None
            temp =temp[1].split("=")
            self.var2=temp[0]
            self.val2=temp[1].split(")")[0]


        except:
            print("line is not fit type 4 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            #print("indexOfVal1=",indexOfVal1)
            #print("indexOfVal2=",indexOfVal2)
        except:
            return False
        variables= list(dataDict.keys())
        x=variables.index(self.func)
        
        if((len(domain[4*x+(indexOfVal1%4)])==1) and (len(domain[4*x+(indexOfVal2%4)])==1)):
            a=int(domain[4*x+(indexOfVal1%4)][0])
            b=int(domain[4*x+(indexOfVal2%4)][0])
            return not (a  < b) 
        
        return False
class Constraints_Type9: #one of {x=a,y=b} corresponds to z=c other t=d
    def __init__(self,var1=None,var2=None,val1=None,val2=None,var3=None,val3=None,var4=None,val4=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.var3=var3
        self.val3=val3 
        self.var4=var4
        self.val4=val4
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 8 ):
            print("constraint type is not fit")
            return None
        try:
            temp=splitted_line[2]
            temp=temp[1:-1]
            temp=temp.split(",")
            self.var1,self.val1=temp[0].split("=")
            self.var2,self.val2=temp[1].split("=")
            self.var3,self.val3=splitted_line[5].split("=")
            self.var4,self.val4=splitted_line[7].split("=")
        except:
            print("line is not fit type 5 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            indexOfVal3=domain.index([self.val3])
            indexOfVal4=domain.index([self.val4])
        except:
            return False
        
        if((indexOfVal1%4 != indexOfVal3%4) and (indexOfVal1%4 != indexOfVal4%4)): # 1 and 3 same subject or 1 and 4 same subject
            return True
        if((indexOfVal2%4 != indexOfVal3%4) and (indexOfVal2%4 != indexOfVal4%4)): #(2and 3) or (2 and 4) same subject
            return True
        if(indexOfVal1%4 == indexOfVal2%4):
            return True
        return False
class Constraints_Type10:#{x=a,y=b,z=c} are all different
    def __init__(self,var1=None,var2=None,val1=None,val2=None,var3=None,val3=None):
        self.var1=var1
        self.var2=var2
        self.val1=val1
        self.val2=val2
        self.var3=var3
        self.val3=val3 
    def createConstaintsFromLine(self,line):
        if(line==None):
            print("line is none")
            return None
        
        splitted_line=line.split()
        if(len(splitted_line)!= 4 ):
            print("constraint type is not fit")
            return None
        try:
            temp=splitted_line[0]
            temp=temp[1:-1] #cut { and }
            temp = temp.split(",")
            self.var1,self.val1=temp[0].split("=")
            self.var2,self.val2=temp[1].split("=")
            self.var3,self.val3=temp[2].split("=")
        except:
            print("line is not fit type 5 constraints")
            
    def isConstraintViolated(self,domain,dataDict):
        try:
            indexOfVal1=domain.index([self.val1])
            indexOfVal2=domain.index([self.val2])
            indexOfVal3=domain.index([self.val3])
        except:
            return False
        
        if(indexOfVal1%4 ==indexOfVal2%4):
            return True
        if(indexOfVal2%4 == indexOfVal3%4):
            return True
        if(indexOfVal1%4 == indexOfVal3%4):
            return True
        return False
class CSPNode:
    def __init__(self, solution=[],domains=[]):
        self.children = [] 
        self.solution = solution
        self.domains  = domains 

class CSPPuzzle:
    indexOfDomains=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #initially domains
    Root = CSPNode([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],indexOfDomains) # initially solution and domains is equal to [0,0,0,...0]
    constraintBase=[]
    dataDict={}
    
    #fill the indexOfDomains with real domain, initialize constraint base and dataDict
    def __init__(self,fileNumber):
        dataFileName="data-"+fileNumber+".txt"
        clueFileName="clues-"+fileNumber+".txt"
        self.dataDict=self.initializeDataDict(dataFileName) #pull data from file
        #print(self.dataDict)
        self.constraintBase = self.initializeConstraintBase(clueFileName) #pull constraints from file 
        #for i in self.constraintBase:            #newNode.printNode()
        #    print("---",i.toString())
        variables =[] 
        for k in self.dataDict:
            variables.append(k)
        #print("variables =",variables)
        #index of domains fill with all values
        n=0
        for var in variables:
            #print("var=",var)
            self.indexOfDomains[n] = self.dataDict.get(var).copy()
            self.indexOfDomains[n+1] = self.dataDict.get(var).copy()
            self.indexOfDomains[n+2] = self.dataDict.get(var).copy()
            self.indexOfDomains[n+3] = self.dataDict.get(var).copy()
            n+=4
    #delegate the initialization of datadict
    def initializeDataDict(self,filename):
        return self.initialize_dict_from_dataLinesArray(self.txtToArray(filename))
    #delegate the initialization of ConstraintBase
    def initializeConstraintBase(self,fileName):
        return self.initialize_constraints_from_linesArray(self.txtToArray(fileName))
    
    def solve(self): 
        print("Puzzle is solving...")
        self.makeAssignment(self.Root,0)
    # first value in domain assign to solution array index 0 and continue to assignment index+1 until constraint not violate. If solution is complete then system exit, otherwise backtrack.
    def makeAssignment(self,node,index): # program working on deep copies because of avoiding side effect
        current_domain = copy.deepcopy(node.domains[index]) #inside domains may change [2006,2007,2008,2009] [2006,2007,2008,2009] 
        copyDomain = copy.deepcopy(node.domains)  #[[1,2,3,4],[1,2,3,4]...]
        for possibleValue in current_domain:
            possibleSolution = copy.deepcopy(node.solution)
            possibleSolution[index] = possibleValue  #assignment is done
            new_domain = self._shrinkDomain(copyDomain, index, possibleValue) #value is removed from relevant domains
            newNode = CSPNode(possibleSolution,new_domain)
            isValidAssignment=True
            for cons in self.constraintBase: #possible solution check constraints
                if(cons.isConstraintViolated(new_domain,self.dataDict)):
                    isValidAssignment=False
                    break
            #if(isValidAssignment):
            #    node.addChildren(newNode)
            if(0 in possibleSolution):
                if(isValidAssignment):    
                    self.makeAssignment(newNode,index+1)
            else:
                for cons in self.constraintBase: #complete solution check constraints 
                    if(cons.isConstraintViolated(new_domain,self.dataDict)):
                        isValidAssignment=False
                        break
                    if(isValidAssignment): # solution found
                        print(possibleSolution[0],possibleSolution[4],possibleSolution[8],possibleSolution[12])
                        print(possibleSolution[1],possibleSolution[5],possibleSolution[9],possibleSolution[13])
                        print(possibleSolution[2],possibleSolution[6],possibleSolution[10],possibleSolution[14])
                        print(possibleSolution[3],possibleSolution[7],possibleSolution[11],possibleSolution[15])
                        sys.exit("Solution is Found")
	
	#assigned value remove from other domains
    def _shrinkDomain(self,domain,x,possibleValue):
        copyDomain = copy.deepcopy(domain)
        n=0
        if(x<4):
            n=0
        elif(x<8):
            n=4
        elif(x<12):
            n=8
        else:
            n=12
        for i in range(n,n+4):
            if(i==x):
                if(possibleValue in copyDomain[x]):
                    copyDomain[i]=[possibleValue]
            else:
                if(possibleValue in copyDomain[i] and len(copyDomain[i]) != 1): 
                    copyDomain[i].remove(possibleValue)
        return copyDomain
    #FileIO -> read file and return lines array
    def txtToArray(self,fileName):
        try:
            f = open(fileName, "r")
            line = f.readline()
            line=line.rstrip("\n")
            linesArray  = []
            while line :
                linesArray.append(line)
                line = f.readline()
                line=line.rstrip("\n")
            f.close()
            return linesArray
        except:
            print("file error")
    
    # initialize constraints Array  -> Constraints array contains constraint objects
    def initialize_constraints_from_linesArray(self,linesArray):
        constraintsBase=[]
        try:    
            for i in linesArray:
                constraintsBase.append(self.initializeConstraintAccoringToline(i))
            return constraintsBase    
        except:
            print("initializing error")
    
    # given line becomes the constraint object
    def initializeConstraintAccoringToline(self,line):
        splitted_line = line.split()
        if(splitted_line[0]=="if"):
            if("not" in splitted_line):                                 #if x=a then not y=b
                constraint=Constraints_Type2() 
            elif("either" in splitted_line):                            #if x=a then either y=b or z=c
                constraint=Constraints_Type3() 
            elif("then" in splitted_line):                              #if x=a then y=b
                constraint=Constraints_Type1()
            else:
                print("error! line is not fit any constraint type")
        else:
            if(len(splitted_line)==3):
                if("=" in splitted_line):                               #n(x=a) = n(y=b) 
                    constraint=Constraints_Type4()
                elif("<" in splitted_line):                             #n(x=a) < n(y=b) 
                    constraint=Constraints_Type8()
                elif(">" in splitted_line):                             #n(x=a) > n(y=b) 
                    constraint=Constraints_Type7()
                else:
                    print("error! line is not fit any constraint type")
            elif(len(splitted_line)==5):
                if("+" in splitted_line):                               #n(x=a) = n(y=b) + m
                    constraint=Constraints_Type5()
                elif("-" in splitted_line):                              #n(x=a) = n(y=b) - m
                    constraint=Constraints_Type6()
                else:
                    print("error! line is not fit any constraint type")
            elif(len(splitted_line)==8):
                constraint=Constraints_Type9()                          #one of {x=a,y=b} corresponds to z=c other t=d
            elif(len(splitted_line)==4):
                constraint=Constraints_Type10()                         #{x=a,y=b,z=c} are all different
            else:
                    print("error! line is not fit any constraint type")
        constraint.createConstaintsFromLine(line)
        return constraint
    
    #initialize data Dictionary {var1:values,var2:values,var3:values,var4:values}
    def initialize_dict_from_dataLinesArray(self,linesArray):
        try:
            data_dict={}
            for i in range(len(linesArray)):
                splitted_line=linesArray[i].split(",")
                data_dict.update({splitted_line[0]:splitted_line[1:]})
            return(data_dict)
        except:
            print("initializing dictionary error")
class App:
    def main(self):
        x=self.inputInteger("Choose a puzzle 1 or 2 or 3:")
        while(x==None):
            x=self.inputInteger("Choose a puzzle 1 or 2 or 3:")
        
        try:
            puzzle=CSPPuzzle(str(x))
            puzzle.solve()
        except SystemExit:
            print("------------Puzzle is solved--------")
        except:
            print("ERROR! \n please try again.")
            self.main()
    def inputInteger(self,text):
        user_input = input(text)
        print("\n")
        try:
            val = int(user_input)
            return val
        except ValueError:
            print("input is not an integer.")
            return None

if __name__ == '__main__':
    app = App()
    app.main()
