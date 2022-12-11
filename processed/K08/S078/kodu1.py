from random import sample

def bingo():
    while True:
        x = sample(range(1, 11), 3)
        järjend = x + sample(range(11, 21), 2)
        if sorted(x) == [1, 2, 3]:
            continue
        else:
            return järjend
            break
    
print(bingo())