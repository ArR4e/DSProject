import random
import string
def suurväike(sõne):
    str = ''
    järjend = []
    result = string.punctuation
    for i in result:
        järjend.append(i)
    tähemärk = random.choice(järjend)
    for i in sõne:
        if i in järjend:
            i = i.replace(i, tähemärk)
        elif i.islower():
            i = i.upper()
        elif i.isupper():
            i = i.lower()
        str += i
    return(str)

    
sõne = input("Sisesta sõne: ")
print(suurväike(sõne))
