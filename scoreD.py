#!/usr/bin/python3
class Node :
    def __init__(self, AsNumber,list):
        self.AsNumber = AsNumber
        self.enfant = list
      
 
def NotcontainChild(toVerify, listEnfant):
    if(listEnfant==[]):
        return True
    for i in listEnfant :
        if(i.AsNumber== toVerify):
            return False
        else :
            return True

def makeGraph(file):
    

    with open(file, 'r') as f:
        lines = f.read().splitlines()
        if (lines == []):
            return False
        nombreAs = 0
        nombreAsPath = len(lines)
        As = [] #liste avec tous les as
        AspathReverse = [] #liste de liste avec les as path inverse (l origine en premier)
        origine = Node(lines[0].split(' ')[-1],[])
        pred = origine
        for asPath in lines:
            reverse=[]
            
            for ase in asPath.split(' ') :
                reverse.append(int (ase)) 
                if (int (ase) not in As):
                    As.append(int (ase))
                    nombreAs+=1
            reverse.reverse ()         
            AspathReverse.append(reverse)
            As = [origine]
            
        index = 0
        for i in AspathReverse :
            while(index < len(i)-1):
                if (NotcontainChild(i[index+1], pred.enfant)):
                    temp = Node(i[index+1],[])
                    pred.enfant.append(temp)
                    As.append(i[index+1])
                    pred = temp
                else :
                    pred = pred.enfant[0]
                index+=1

            index=0
            pred = origine            
        return origine        
        
def fusion(node): # node = origine
    
    if(node.enfant == []):
        return False
    pred = node.enfant[0] # pred = a1
    b = False
    for i in node.enfant: # i = a1 pour la premiere iteration, ensuite a2,... 
        if(i.AsNumber != pred.AsNumber): #on verifie aue pred et i sont pas les memes as
            for j in i.enfant: #on verifie que les 2 enfants fusionnent 
                if(j in pred.enfant ):
                    return [pred,i]
            pred = i # pred = l enfant suivant 
                
    return 0
            

def diversity(origine):
    if not(origine):
        return  "There is no as path between this pair of AS"
    
    f = False
    d = 0
    if(origine.enfant==[]) :
        return 1
    for i in origine.enfant :
        if(fusion(origine)!=0 and f==False):
            frere = (fusion(origine)[0])
            soeur = (fusion(origine)[1])
            d = diversity(frere)*diversity(soeur)
            f = True
            
        else :
            dc = 0.5*diversity(i)
            d = d +dc - d*dc
    return d      
        
vo = makeGraph("output.txt")
print(diversity(vo))
