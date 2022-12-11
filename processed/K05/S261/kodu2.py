import string
import random

def suurväike(sona):
    x=list(sona)
    y=string.punctuation[random.randint(0,20)]
    for i in range(len(x)):
        if x[i] in string.punctuation:
            x[i]=y            
        elif x[i].isupper()==True:
            x[i]=x[i].lower()
        else:
            x[i]=x[i].upper()
    return(''.join(x))
            
sona=input('Sisesta oma lause:')
print(suurväike(sona))

