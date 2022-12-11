from random import sample

def bingo():
    while True:
        nums_1 = sample(range(1, 11), 3)
        nums_2 = sample(range(11, 21), 2)
        if sorted(nums_1) != [1, 2, 3]:
            break
     
    return nums_1 + nums_2