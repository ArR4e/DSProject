import string, random
def suurväike(sisse):
    uus_märk = random.choice(string.punctuation)
    uus=""
    for i in sisse:
        if i not in string.punctuation:
           uus = uus+i
        else:
            uus = uus + uus_märk
    vahetus = uus.swapcase()
    return (vahetus)


suurväike(input("Sisestage palun üks sõna või lause: "))
