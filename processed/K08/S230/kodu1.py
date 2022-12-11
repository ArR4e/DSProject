from random import sample

def bingo():
    while True:
        a=(sample(range(1,11),3))
        kontroll=sorted(a)
        if kontroll!=[1,2,3]:
            break
    b=(sample(range(11,21),2))
    return a+b
print(bingo())