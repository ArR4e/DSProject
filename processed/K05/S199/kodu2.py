import string
import random


def suurväike(lause):
    tähed = ""
    for täht in lause:
        if täht.isupper() == True:
            täht = täht.lower()
            tähed += str(täht)
        elif täht.islower() == True:
            täht = täht.upper()
            tähed += str(täht)
        elif täht == (" "):
            täht = " "
            tähed += str(täht)
        else:
            täht = string.punctuation
            tähed += str(täht)
    return(tähed)