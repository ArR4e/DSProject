from random import sample

def bingo():
    väiksed=sample(range(1,11),3)
    while sorted(väiksed)==[1,2,3]:
        väiksed=sample(range(1,11),3)
    suured=sample(range(11,21),2)
    return(väiksed+suured)