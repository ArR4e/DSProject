from random import sample
jrj = []
def bingo():
    a = sample(range(1,11), 3)
    while [1, 2, 3] in a:
        a = sample(range(1,11), 3)
        
    b = (sample(range(11,21), 2))
    jrj = a+ b
    return jrj

print(bingo())
    
    
    