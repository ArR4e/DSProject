import string
import random

def suurväike(lause):
    uus_lause = ""
    märk = random.choice(string.punctuation)
    for täht in lause:
        if täht in string.punctuation:
            uus_lause += märk
        else:
            uus_lause += täht.swapcase()
    print(uus_lause)
    return uus_lause

suurväike("E/!!¤")