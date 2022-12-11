import string
from random import randint
def suurväike(x):
    rand_number = randint(0, len(string.punctuation))
    y = string.punctuation[rand_number]
    for el in x:
        if el.isalpha() == False and el != ' ' and el.isnumeric() == False:
            x = x.replace(el, y)
    x = x.swapcase()
    return(x)       