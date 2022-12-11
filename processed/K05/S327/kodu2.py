from random import randint
def suurväike(sõne):
    uus_sõne = ""
    punc = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    random = randint(0,31)
    for tähemärk in sõne:
        if str.islower(tähemärk) == True:
            uus_sõne += tähemärk.upper()
        elif str.isupper(tähemärk) == True:
            uus_sõne += tähemärk.lower()
        elif tähemärk in punc:
            uus_sõne += punc[random]
        elif tähemärk == " ":
            uus_sõne += " "
    return uus_sõne