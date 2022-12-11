from random import sample

def bingo():
    return a + b
    
a = sample(range(1, 11), 3)
b = sample(range(11, 21), 2)
    
for element in a:
    if a == 1 and a == 2 and a == 3:
        a = sample(range(1, 11), 3)
    else:
        break
    
print(bingo())