from random import sample

def bingo():
    
    a = sample(range(1,11), 3)
    b = sample(range(11,21), 2)
    
    for x in b:
       a.append(x)
    
    while True:
        if 1 in a:
            if 2 in a:
                if 3 in a:
                    a = sample(range(1,11), 3)
                    b = sample(range(11,21), 2)
                    
                    for x in b:
                        a.append(x)
                else:
                    break
            else:
                break
        else:
            break
    
    return a