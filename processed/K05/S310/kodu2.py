import string
import random


def suurväike(s):
    newStr = ""
    randomSymbol = random.choice(string.punctuation)
    
    i = 0
    while(i < len(s)):
        char = s[i]
        
        if char.isupper():
            newStr += char.lower()
        elif char.islower():
            newStr += char.upper()      
        elif char in string.punctuation:
            newStr += randomSymbol
        else:
            newStr += char
        i += 1
        
    return newStr

    
print(suurväike("LIn,A,,asd"))