from random import*
def bingo():
    järjend = []
    i = 0
    while i < 3:
        arv = randint(1, 10)
        while arv in järjend:
            arv = randint(1, 10)
        järjend += [arv]
        i += 1
    while [1] in järjend and [2] in järjend and [3] in järjend:
        järjend = []
        i = 0
        while i < 3:
            arv = randint(1, 10)
            while arv in järjend:
                arv = randint(1, 10)
            järjend += [arv]
            i += 1
    järjend += [randint(11, 20)]
    arv = randint(11, 20)
    while arv in järjend:
        arv = randint(11,20)
    järjend += [arv]
    return järjend
    

    
        
    