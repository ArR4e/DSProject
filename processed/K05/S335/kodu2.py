import string
from random import choice
def suurväike(a):
    sõne = ""
    for täht in range(0, len(a)):
        if a[täht].islower():
            sõne += a[täht].upper()
        elif a[täht].isupper():
            sõne += a[täht].lower()
        elif a[täht] == " ":
            sõne += " "
        else:
            sõne += choice(string.punctuation)
    return sõne