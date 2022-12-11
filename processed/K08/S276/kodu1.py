from random import sample
def bingo():
    a=sample(range(1, 11), 3)
    b=sample(range(11, 21), 2)
    arvud=a+b
    while 1 and 2 in arvud or 1 and 3 in arvud or 2 and 3 in arvud:
        a=sample(range(1, 11), 3)
        b=sample(range(11, 21), 2)
        arvud=a+b
        continue
    return arvud
