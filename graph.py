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
        #print (lines)
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
                #if(i[index+1] not in pred.enfant):
                if (NotcontainChild(i[index+1], pred.enfant)):
                    
                   # print("pred ", pred.AsNumber, "i ", i[index+1], "enfant", pred.enfant)
                    temp = Node(i[index+1],[])
                    pred.enfant.append(temp)
                    As.append(i[index+1])
                    pred = temp
                else :
                    pred = pred.enfant[0]
                index+=1

            index=0
            pred = origine
           # print(pred.AsNumber)
                
              # print(AspathReverse )
     #  print(nombreAsPath)
       # print("origine "+ origine.AsNumber)
       # print("0",origine.enfant[0].AsNumber)
        #print("1",origine.enfant[1].AsNumber)
        #print("2",origine.enfant[2].AsNumber)
        #print("3",origine.enfant[3].AsNumber)
        #print("enfant de 6453",origine.enfant[3].enfant[0].AsNumber)
        #print("enfant de 29571",origine.enfant[1].enfant[0].AsNumber)
        #print("enfant de 8346",origine.enfant[2].enfant[0].AsNumber)
        #print("enfant de 6713",origine.enfant[0].enfant[0].AsNumber)
        #print("enfant de 6713",origine.enfant[0].enfant[1].AsNumber)
        #print("enfant de 174",origine.enfant[0].enfant[1].enfant[0].AsNumber)
        #print("enfant de 174",origine.enfant[0].enfant[0].enfant[0].AsNumber) 
        #print("enfant de 5511",origine.enfant[1].enfant[0].enfant[0].AsNumber)             
        return origine        
        
def fusion(node): # node = o
    
    if(node.enfant == []):
        return False
    pred = node.enfant[0] # pred = a1
    b = False
    for i in node.enfant: # i = a1 pour la premiere iteration, ensuite a2,... 
        if(i.AsNumber != pred.AsNumber): #on verifie aue pred et i sont pas les memes as
            for j in i.enfant: #on verifie que les 2 enfants fusionnent 
                if(j in pred.enfant ):
                  #  print("pred.AsNumber ", pred.AsNumber)
                   # print(pred.AsNumber ,i.AsNumber)
                  #  print("fusion")
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
            print("fusion")
            d = diversity(frere)
            f = True
            
        else :
            dc = 0.5*diversity(i)
            d = d +dc - d*dc
    return d
        
        
origine = makeGraph("output.txt")
print(diversity(origine))
