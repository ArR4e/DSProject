from random import sample
def bingo():
    tagasta = []
    tagasta += sample(range(1,11),3)
    tagasta += sample(range(11,21),2)
    if 3 in tagasta and 2 in tagasta and 1 in tagasta:
        tagasta = bingo()
    return tagasta