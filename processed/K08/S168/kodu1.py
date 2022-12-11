from random import sample

def bingo():
    list = []
    while True:
        list += sample(range(1, 11), 3)
        list += sample(range(11, 21), 2)
        if not ((1 in list) and (2 in list) and (3 in list)):
            break
    return(list)

print(bingo())
        
        