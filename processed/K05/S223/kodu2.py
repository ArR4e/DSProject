import string
from random import randint

def suurväike(lause):
    uus_lause = ""
    märgid = list(string.punctuation)[randint(0,31)]
    for x in range(len(lause)):
        if lause[x] in väikesed:
            uus_lause += lause[x].upper()
        elif lause[x] in suured:
            uus_lause += lause[x].casefold()
        else:
            if lause[x] == " ":
                uus_lause += " "
            else:
                uus_lause += märgid
    return uus_lause
            


väikesed = list(string.ascii_lowercase)
suured = list(string.ascii_uppercase)

print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))
