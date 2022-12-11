from random import sample


def bingo():
    while True:
        
        j1=sample(range(1, 11), 3)
        j2=sample(range(11, 21), 2)
        tulemus=[]
        tulemus.extend(j1)
        tulemus.extend(j2)
        if 1 in tulemus and 2 in tulemus and 3 in tulemus:
            bingo()
        else:
            return tulemus
            break


        
    
    
        
        
    