from random import randint
def suurväike(sõne):
    uus=''
    import string
    punct=string.punctuation[randint(0,32)]
    for el in sõne:
        if el in string.punctuation:
            uus+=punct
        elif el.isupper()==True:
            uus+=el.lower()
        elif el.islower()==True:
            uus+=el.upper()
        elif el==' ':
            uus+=' '
    return uus
