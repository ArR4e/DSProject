from random import sample

def bingo():
    while True:
        jarjend=sample(range(1,11),3)
        if {1,2,3}.issubset(jarjend):
            continue
        else:
            break
    jarjend.extend(sample(range(11, 21),2))
    return(jarjend)
