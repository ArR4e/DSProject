from random import sample

def bingo():
    numbrid=[]
    while True:
        esimesed=sample(range(1, 11), 3)
        if 1 in esimesed and 2 in esimesed and 3 in esimesed:
            continue
        else:
            numbrid+=esimesed
            break
    ülejäänud=sample(range(11, 21), 2)
    numbrid+=ülejäänud
    return numbrid
