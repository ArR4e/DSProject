from random import sample
import random

def bingo():
    numbrid1=sample(range(1, 11), 3)
    numbrid2=random.randint(11,20)
    numbrid3=random.randint(11,20)
    arvud=numbrid1+[numbrid2]+[numbrid3]
    print(arvud)
bingo()