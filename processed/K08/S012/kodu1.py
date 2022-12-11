#kodu1
from random import sample
def bingo():
    järj1 = sample(range(1, 11), 3)
    while (1 in järj1) and (2 in järj1) and (3 in järj1):
        järj1 = sample(range(1, 11), 3)
    järj2 = sample(range(11, 21), 2)
    järjend = järj1 + järj2
    return järjend
    
                   