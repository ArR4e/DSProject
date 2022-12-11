import random
import string
def suurväike(sõne):
    a=0
    b=len(sõne)
    suv=random.choice(string.punctuation)
    while b>a:
        c=sõne[a]
        a+=1
        if c==" ":
            print (" ",end="")
        elif bool(c==c.upper()) == bool(c==c.lower()):
            print (suv,end="")
        elif bool(c==c.upper()) == True:
            print (c.lower(), end="")
        elif bool(c==c.lower()) == True:
            print (c.upper(),end="")
