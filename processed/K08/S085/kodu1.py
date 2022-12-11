from random import sample

def bingo():
    
    while True:
        a = sample(range(1,11), 3)
        if [1,2,3] == a:
            continue
        elif [1,3,2] == a:
            continue
        elif [2,3,1] == a:
            continue
        elif [2,1,3] == a:
            continue
        elif [3,2,1] == a:
            continue
        elif [3,1,2] == a:
            continue
        else:
            b = sample(range(11,21), 2)
        return a+b
bingo()