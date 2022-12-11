import string
import random

s = input("Sisesta lause: ")
def suurväike (s):
    
    new_str=""
    märgid = random.choice(string.punctuation)
    
    for i in range (len(s)):
        if s[i].isupper():
            new_str+=s[i].lower()
        elif s[i].islower():
            new_str+=s[i].upper()
        elif s[i].isspace():
            new_str += " "
        else:
            new_str+=märgid
    return(new_str)
    
suurväike(s)