from random import sample

def bingo():
    def kontrolli(a):
        if 1 in a and 2 in a and 3 in a:
            return False
        else:
            return True
    while True:
        a = sample(range(1,11), 3) + sample(range(11,21), 2)
        if kontrolli(a):
            return a