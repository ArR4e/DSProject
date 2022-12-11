from random import randint
import string
def suurväike(n):
    a = randint(0, len(string.punctuation))
    word = ''
    for i in n:
        if i.isupper():
            word += str(i).lower()
        if i.islower():
            word += str(i).upper()
        if i == ' ':
            word += ' '
        if i in string.punctuation:
            word += str(string.punctuation[a])
    return word
    
a = suurväike('John vastas: "Hilja, peremees, hilja."')
