import random
import string
def suurväike(x):
    sõna=''
    kvm = random.choice(string.punctuation)
    for i in x:
        if i.isupper():
            i = i.lower()
            sõna=sõna+str(i)
        elif i.islower():
            i = i.upper()
            sõna=sõna+str(i)
        elif i==' ':
            sõna=sõna+' '
        else:
            for m in string.punctuation:
                if i == m:
                    i = i.replace(i, kvm)
                    sõna = sõna+str(i)
                    break
                else:
                    continue
    return(sõna)