from random import sample

def bingo():
    while True:
        a =sample(range(1,11),3)
        b = sample(range(11,21),2)
        järjend = a + b
        korras = 0
        if 1 in järjend[0:3] and 2 in järjend[0:3] and 3 in järjend[0:3]:
            print("Genereeritakse uus järjend")
            järjend = []
        else:
            return järjend
            break

print(bingo())