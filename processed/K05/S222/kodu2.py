import string
from random import choice

def suurväike(a):
    n = 0
    a = list(a)
    for m in a:
        if m not in string.ascii_lowercase and m not in string.ascii_uppercase and not m.isnumeric() and m != " ":
            a[n] = choice(string.punctuation)
        n += 1
    return "".join(a).swapcase()

print(suurväike("MinA oleN Tubli!!"))
print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))