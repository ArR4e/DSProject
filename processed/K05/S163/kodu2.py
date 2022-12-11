from random import *

märgid = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def suurväike(sõne):
    uusMärk = märgid[randint(0, len(märgid))]
    uusSõne = ''
    for i in sõne:
        if i in märgid:
            uusSõne += uusMärk
        elif i.islower() == True:
            i = i.upper()
            uusSõne += i
        else:
            i = i.lower()
            uusSõne += i
    return uusSõne
            
print(suurväike("Uus-Meremaa"))