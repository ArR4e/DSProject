from random import sample
def bingo():
    numbrid=[]
    while True:
        a=sample(range(1,11),3)
        if 1 in a and 2 in a and 3 in a:
            continue
        else:
            numbrid+=a
            break
    b=sample(range(11,21),2)
    numbrid+=b
    return numbrid