import string
import random

def suvamärk():
    suva=random.choice(string.punctuation)
    return suva

def suurväike(a):
    b=''
    a=a.strip('\n')
    märk = suvamärk()
    for i in a:
        if i.isalpha():
            if i.isupper():
                i=i.lower()
                b+=i
            elif i.islower():
                i=i.upper()
                b+=i
        elif i == ' ':
            b+=i
        else:
            b+=märk
            
    return b