import string
import random
def suurväike(myString):
    punctuation=string.punctuation
    valik=random.choice(string.punctuation)
    for c in myString:
        if c in punctuation:
            newString = myString.replace(c, valik)
            swapped_string=newString.swapcase()
    print(swapped_string)


