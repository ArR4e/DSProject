from random import sample

def bingo():
    järjend = []
    järjend[0:2]=sample(range(1, 11), 3)
    järjend[3:5]=sample(range(11, 21), 2)
    for sum in [0,1,2]:
        if sum == 6:
            continue
    return järjend

print(bingo())
   