import string, random
def suurväike(x):
    x = x.swapcase()
    y = random.choice(string.punctuation)
    for i in x:
        if i in string.punctuation:
            x = x.replace(i, y)

    return(x)
    