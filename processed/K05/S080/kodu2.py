def suurväike (sõne):
    import string
    import random
    a = 0
    c = ''
    b = len(sõne)
    e = random.choice(string.punctuation)
    while a<b:
        d = sõne[a]
        a = a+1
        if d.isupper():
            d = d.lower()
            c = c + d
        elif d.islower():
            d = d.upper()
            c = c + d
        elif d in string.punctuation:
            #d = d.replace(d,random.choice(string.punctuation))
            d = d.replace(d,e)
            c = c + d
        else:
            c = c + d
    return(c)
suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")