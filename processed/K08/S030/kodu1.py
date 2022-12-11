def bingo():
    while True:
        from random import sample
        lst1=sample(range(1,11),3)
        lst2=sample(range(11,21),2)
        lstf=lst1+lst2
        if sum(lst1)!=6:
            break
    return lstf