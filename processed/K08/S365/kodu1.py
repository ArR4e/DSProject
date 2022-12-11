from random import sample

def bingo():
    jada = []
    x = sample(range(1, 11), 3)
    y = sample(range(11, 21), 2)
    for m in x:
        jada.append(m)
    for n in y:
        jada.append(n)
    return jada
    
print(bingo())
    