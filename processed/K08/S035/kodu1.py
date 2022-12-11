from random import sample
import random
def bingo():
    arvud=[]
    numbrid = sample(range(1, 11), 3)
    if 1 in numbrid:
        if 2 in numbrid:
            if 3 in numbrid:
                numbrid = sample(range(1, 11), 3)                
    numbrid2 = sample(range(11, 21), 2)
    arvud=numbrid + numbrid2
    return(arvud)
