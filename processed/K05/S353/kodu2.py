from string import punctuation
from random import choice
def suurväike(k):
    i=0
    tag=''
    x= choice(punctuation)
    while i<len(k):
        tähemärk=k[i]
        if tähemärk.isupper():
            tag+=tähemärk.lower()
        elif tähemärk.islower():
            tag+=tähemärk.upper()
        elif tähemärk in punctuation:
            tag+=x
        else:
            tag+=tähemärk
        i+=1
    return tag
#print(suurväike("MinA oleN Tubli!!"))