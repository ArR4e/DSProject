from random import sample

def bingo():
    cs = True
    bin = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    
    while cs == True:
        for el in bin:
            if el == 1 or el == 2 or el == 3:
                if bin[bin.index(el) +1] == 1 or bin[bin.index(el) +1] == 2 or bin[bin.index(el) +1] == 3:
                    if bin[bin.index(el) +1] == 1 or bin[bin.index(el) +1] == 2 or bin[bin.index(el) +1] == 3:
                        bin = sample(range(1, 11), 3) + sample(range(11, 21), 2)
                    else:
                        cs = False
                else:
                    cs = False
            else:
                cs = False
    return bin
        