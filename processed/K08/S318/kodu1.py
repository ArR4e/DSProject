from random import sample

def bingo():
    sam1=(sample(range(1,11), 3))
    sam2=(sample(range(11,21), 2))
    sam=sam1+sam2
    if sam1 == [1,2,3] or sam1 == [1,3,2] or sam1 == [2,1,3] or sam1 == [2,3,1] or sam1 == [3,1,2] or sam1 == [3,2,1]:
        sam2=(sample(range(1,11), 3))+(sample(range(11,21), 2))
        return sam2
    else:
        return sam