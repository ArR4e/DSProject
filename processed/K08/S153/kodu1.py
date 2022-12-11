from random import sample
def bingo():
    l1 = sample(range(1, 11), 3)
    l2 = sample(range(11, 21), 2)
    string_ints = [str(int) for int in l1]
    string_ints = [str(int) for int in l2]
    l1.extend(l2)
    if set([1, 2, 3]).issubset(l1) == True:
        bingo()
    else:
        return l1