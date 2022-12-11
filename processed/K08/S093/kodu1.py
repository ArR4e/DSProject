from random import sample

def bingo():
    while True:
        repeat = False
        järjend = sample(range(1, 11), 3)
        järjend_1 = sample(range(11, 21), 2)
        lõpp_jär = järjend + järjend_1
        for i in range(1, 4):
            if lõpp_jär[i] - 1 == lõpp_jär[i-1] and lõpp_jär[i] + 1 == lõpp_jär[i+1]:
                repeat = True
        if not repeat:
            return lõpp_jär
# bingo()