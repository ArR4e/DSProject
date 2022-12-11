from random import sample
def bingo():
    väiksed=sample(range(1,11),3)
    while True:
        if 1 in väiksed and 2 in väiksed and 3 in väiksed:
            väiksed=sample(range(1,11),3)
        else:
            break
    suured=sample(range(11,21),2)
    järjend=väiksed+suured
    return(järjend)
bingo()