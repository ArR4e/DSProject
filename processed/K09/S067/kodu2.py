from random import randint
def minu_shuffle(x):
    if x == []:
        print('Sisesta mitte tühi list!')
    else:
        y = randint(len(x), len(x) * 3)
        i = 0
        while i <= y:
            x.append(x.pop(int(randint(0, len(x) - 1))))
            i += 1
minu_shuffle([])