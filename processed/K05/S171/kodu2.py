import string
from random import*

def suurväike(x):
    vastus = ""
    märk = string.punctuation[randint(0, len(string.punctuation)-1)]
    for i in x:
        if i in string.punctuation:
            vastus += märk
        elif i.isupper():
            vastus += i.lower()
        elif i.islower():
            vastus += i.upper()
        elif i == " ":
            vastus += " "
    return vastus
            
a = input()
print(suurväike(a))

