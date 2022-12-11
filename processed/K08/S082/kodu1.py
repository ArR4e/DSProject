from random import sample

def bingo():
    a = sample(range(1, 10), 3)
    a = [1, 3, 2]
    b = sample(range(11, 20), 2)
    if 1 in a and 2 in a and 3 in a:
        a = sample(range(1, 10), 3)
        b = sample(range(11, 20), 2)
        nimekiri = (a + b)
    else:
        nimekiri = (a + b)
    
    
    return nimekiri
    


print(bingo())