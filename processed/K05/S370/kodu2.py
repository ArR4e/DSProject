import string
import random
def suurväike(s):
    k=random.choice(string.punctuation)
    s=list(s)
    b=0
    sõna=""
    for i in s:
        if i.isupper() == True:
            s[b]=i.lower()
        else:
            if i.islower() == True:
                s[b]=i.upper()
        if i in string.punctuation:
            s[b]=k
        b+=1
    for i in s:
        sõna+=i
    return sõna
               

a= input("Anna sõna, kus suur- ja väiketähed ära vahetada: ")

print(suurväike(a))

##oleks saanud palju lihtsamalt .swapcase() käsuga, aga tahtsin listidega harjutada