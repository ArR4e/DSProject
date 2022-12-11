#bingo ülesanne
from random import sample
 
def bingo():
    vaikesed = sample(range(1, 11), 3)
    
    while sorted(vaikesed) == [1,2,3]:
        vaikesed = sample(range(1, 11), 3)
    
    suured = sample(range(11, 21), 2)
    print(vaikesed + suured)