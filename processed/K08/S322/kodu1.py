from random import sample
def bingo():
    arvud = [1, 2, 3]
    # genereeri seni, kuni list pole enam [1, 2, 3]
    while 1 in arvud and 2 in arvud and 3 in arvud:
        arvud = sample(range(1, 11), 3)
    arvud += sample(range(11, 21), 2)
    return arvud
