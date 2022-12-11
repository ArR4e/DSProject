from random import sample

def bingo():
    i = 0
    while i < 1:
        jär_1 = [1,2,3,4,5,6,7,8,9,10]
        jär_2 = [11,12,13,14,15,16,17,18,19,20]
        a = sample(jär_1,3)+sample(jär_2,2)
        b=sorted(a)
        if b[0] == 1 and b[1] == 2 and b[2] == 3:
            continue
        i = 1
        return a
    
print(bingo())