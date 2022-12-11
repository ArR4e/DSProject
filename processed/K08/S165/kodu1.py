from random import sample

def bingo():
    while True:
        arvud1 = sample(range(1,11),3)
        arvud2 = sample(range(11,21),2)
        järjend = arvud1 + arvud2
        
        if 1 in järjend and 2 in järjend and 3 in järjend:
            continue
        else:    
            return järjend



print(bingo())
    

      
   
   
   
   