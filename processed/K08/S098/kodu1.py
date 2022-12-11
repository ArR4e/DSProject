from random import sample
def bingo():
   while True:
        a = []
        a += sample(range(1, 11),3)
        a += sample(range(11, 21),2)
        if a.count(1) == 1 and a.count(2) == 1 and a.count(3) ==1:
            continue
        else:
            break
   return a
bingo()