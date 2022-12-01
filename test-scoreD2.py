#listeAs = [42861,45609,23674,52362,7552,20115,134674,212237,37020,61218,7018,37020,141231,25543,14013,270785]
#7018 3257 23947 38525 9340 140013
#7018 1299 38158 4787 140013
#7018 6453 38158 4787 140013

class Node :
    def __init__(self, AsNumber,list):
        self.AsNumber = AsNumber
        self.enfant = list

#entre as 7018 et 140013, pas ouf diversite
e8 = Node(7018,[])
e9 = Node(3257,[e8])
e7 = Node(23947,[e9])
e6 = Node(1299,[e8])
e5 = Node(6453,[e8])
e4 = Node(38525,[e7])
e3 = Node(38158,[e5,e6])
e2 = Node(9430,[e4])
e1 = Node(4787,[e3])
ori = Node(140013,[e1,e2])


##################entre 42861 et 45609 
#42861 8732 6939 9498 45609
#42861 6939 9498 45609

b4 = Node(42861,[])
b3 = Node(8732,[b4])
b2 = Node(6939,[b3,b4])
b1 = Node(9494,[b2])
o1 = Node(45609,[b1])

#comparaison prof
a6 = Node(6, [])
a5 = Node(5,[a6])
a4 = Node(4,[a6])
a3 = Node(3,[a5])
a21 = Node(21,[a6])
a2 = Node(2,[a21])
a1 = Node(1,[a4])
o = Node(0, [a1,a2,a3])
l = []

#comparaison prof
ac6 = Node(6, [])
ac5 = Node(5,[ac6])
ac4 = Node(4,[ac5])
ac3 = Node(3,[ac4])
ac2 = Node(2,[ac4])
oc = Node(0, [ac2,ac3])

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
            
#print(type(fusion(o)[0]))

def diversity(origine):
    f = False
    d = 0
    if(origine.enfant==[]) :
        return 1
    for i in origine.enfant :
       # print(i.AsNumber)
        if(fusion(origine)!=0 and f==False):
            frere = (fusion(origine)[0])
            soeur = (fusion(origine)[1])
            print("fusion")
            #dc = 0.5*diversity(i)
            #print(frere.AsNumber)
            d = diversity(frere)
            
           # print(dc)
            f = True
            
        
        else :
            
            dc = 0.5*diversity(i)
            print(dc)
            d = d +dc - d*dc
            #d = d +dc 
    return d

print(diversity(oc))