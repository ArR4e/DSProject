import random
import string

def suurväike(a):
    tagasi = ""
    rand = random.randint(0, len(string.punctuation)-1)
    for letter in a:
        if letter in string.punctuation:
            tagasi += string.punctuation[rand]
        elif letter.isupper():
            tagasi += letter.lower()
        elif letter.islower():
            tagasi += letter.upper()
        else:
            tagasi += letter
            
    return tagasi

