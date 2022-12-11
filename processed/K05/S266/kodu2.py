import random
import string
def suurväike(sone):
    mark = random.choice(string.punctuation)
    sone2 = ""
    for i in sone:
        if i.isalpha():
            sone2 += i.swapcase()
        elif i == " ":
            sone2 += " "
        elif i in string.punctuation:
            i = mark
            sone2 += i
    return sone2
           
print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))