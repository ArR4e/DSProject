import string, random
def suurväike(sone):
    i = 0
    uus = list(sone)
    lopp = ""
    for el in uus:
        if el.isupper():
            #sone = sone.replace(el, el.lower())
            uus[i] = el.lower()
        elif el.islower():
            #sone = sone.replace(el, el.upper())
            uus[i] = el.upper()
        else:
            if el not in string.punctuation:
                uus[i] = el
            else:
                suva = random.randint(0, 32)
                sone = sone.replace(el, string.punctuation[suva])
                #uus[i] = string.punctuation[suva]
                uus[i] = sone[i]
        i+=1
    return (lopp.join(uus))