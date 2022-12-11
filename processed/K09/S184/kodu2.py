import random

def minu_shuffle(järjend):
    if järjend==[]:
        return
    else:
        for i in range (0,len(järjend)+1):
             j=random.randint(0,len(järjend)-1)
             e=järjend.pop(random.randint(0,len(järjend)-1))
             järjend.insert(j,e)
        print(str(järjend))
        
järjend=[0,1,2,3,4,5,6]
minu_shuffle(järjend)