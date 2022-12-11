from random import sample
def bingo():
    while True:
        x=sample(range(1,11),3)
        y=sample(range(11,21),2)
        z=x+y
        numbrid=[1, 2, 3]
        result=all(elem in z for elem in numbrid)
        if result:
            continue
        else:
            break
    return z

#https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
