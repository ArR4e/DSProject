from random import randint
def suurväike(sõna):
    sümbolid = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    väikesed = 'qwertyuiopüõasdfghjklöäzxcvbnm'
    suured = 'QWERTYUIOPÜÕASDFGHJKLÖÄZXCVBNM'
    
    koht = randint(0,len(sümbolid))
    sümbol = sümbolid[koht]
    
    uus = ''
    for i in sõna:
        if i in väikesed:
            uus += i.upper()
        elif i in suured:
            uus += i.lower()
        elif i in sümbolid:
            uus += sümbol
        else:
            uus += i
    return uus

print(suurväike("LzG/#o"))