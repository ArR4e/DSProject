from random import sample

def bingo():
    tagastatav = []
    
    for i in range(1):
        x = sample(range(1, 11), 3)
        if sum(x) != 6:
            tagastatav += x
        else:
            x = sample(range(1, 11), 3)
            tagastatav += x
        
        
    for i in range(1):
        y = sample(range(11, 21), 2)
        tagastatav += y
        
    return(tagastatav)
    
print(bingo())
