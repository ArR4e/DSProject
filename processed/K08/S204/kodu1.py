from random import sample
def bingo():
    järjend=[]
    järjend2=[]

    
    järjend[0:2]=sample(range(1, 11), 3)
    b = sum(järjend[0:3])
    while True:
        if b==6:
            järjend2[0:2]=sample(range(1, 11), 3)
            järjend2[3:4]=sample(range(11, 21), 2)
            break
        
        else:
            järjend2[0:2]=järjend[0:3]
            järjend2[3:4]=sample(range(11, 21), 2)
            break
    
    
        
    
    return järjend2
    
    
print(bingo())