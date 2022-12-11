import random

def suurväike(sõne):
    sümbolid = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    sümbol = random.choice(sümbolid)
    rida = ""
    
    for täht in sõne:
        if täht.isupper():
            täht = täht.lower()
       
        elif täht.islower():
            täht = täht.upper()
            
        for suvaline in range(len(sümbolid)):
            if sümbolid[suvaline] == täht:
                täht = sümbol
                
        rida += täht
    return (rida)


print(suurväike("aJ?lkgfFCXD:,b"))


        