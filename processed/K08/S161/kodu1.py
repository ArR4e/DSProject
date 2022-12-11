from random import sample
import random
def bingo():
    x=sample(range(1, 20), 5)
    i=0
    m=0
    for elem in x:
        if x.count(elem) > 1:
            x[x.index(elem)]=random.randrange(1,19)
    if 1 and 2 and 3 in x:
        x[x.index(random.choice([1,2,3]))]=random.randrange(3,19)
    for rida in x:
        if rida>=1 and rida<=10:
            i+=1
        if i>3:
            x[x.index(rida)]=random.randrange(11,19)
    for rida in x:
        if rida>=11:
            m+=1
        if m>2:
            x[x.index(rida)]=random.randrange(1,9)
    for elem in x:
        if x.count(elem) > 1:
            if elem<=10:
                x[x.index(elem)]=random.randrange(1,9)
            if elem>10:
                x[x.index(elem)]=random.randrange(11,19)
    return(x)
print(bingo())