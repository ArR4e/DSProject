from random import sample

def bingo():
    #return sample(range(1, 11), 3).extend(sample(range(11, 21), 2))
    
    tulemus = sample(range(1, 11), 3)
    tulemus.extend(sample(range(11, 21), 2))
    tulemus.sort()
    
    return tulemus if [1, 2, 3] != tulemus[:3] else bingo()

print(bingo())