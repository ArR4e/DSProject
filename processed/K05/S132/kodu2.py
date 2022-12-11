import string
from random import choice


def suurväike(sone):
    mark = choice(string.punctuation)
    list_ = list(sone)
    uus_sone = ""
    for taht in list_:
        if taht.isupper():
            uus_sone += taht.lower()
        elif taht.islower():
            uus_sone += taht.upper()
        elif taht.isspace():
            uus_sone += " "
        else:
            uus_sone += mark
    print(uus_sone)
    return(uus_sone)
    