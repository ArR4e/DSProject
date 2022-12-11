from random import sample
def bingo():
    algus = sample(range(1, 11), 3)
    lõpp = sample(range(11, 21), 2)
    while algus == [1, 2, 3] or algus == [2, 3, 1] or algus == [3, 1, 2] or algus == [1, 3, 2] or algus == [2, 1, 3] or algus == [3, 2, 1]:
        algus = sample(range(1, 4), 3)
    vastus = algus + lõpp
    return(vastus)
   
print(bingo())