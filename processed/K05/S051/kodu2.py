from random import choice
from string import punctuation

def suurväike(sõne):
    kirjavahemärk = choice(punctuation)
    sõne = sõne.swapcase()
    vastus = ""
    
    for i in sõne:
        if not i.isalnum() and i != " ":
            vastus += kirjavahemärk
        else:
            vastus += i
    return vastus