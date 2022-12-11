from random import sample

def bingo() :
    lotonumbrid = []
    esimesed_numbrid = sample(range(1, 11), 3)
    while esimesed_numbrid == [1, 2, 3] :
        esimesed_numbrid = sample(range(1, 11), 3)
    lotonumbrid += esimesed_numbrid
    teised_numbrid = sample(range(11, 21), 2)
    lotonumbrid += teised_numbrid
    return lotonumbrid