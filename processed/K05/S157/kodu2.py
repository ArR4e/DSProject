from random import randint
import string
def suurväike(x):
    margid = string.punctuation
    juhusmark= margid[randint(0, len(margid)-1)]
    for i in x:
        if i in margid:
            x= x.replace(i, juhusmark)
    return x.swapcase()







sona=input("Sisesta mingi sona: ")
suurväike(sona)
print(suurväike(sona))
