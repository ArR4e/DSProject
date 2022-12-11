import string
import random

def suurväike(sõne):
    asendus = ""
    kirjavahemärk = random.choice(string.punctuation)
    for i in sõne:
        if i.isupper():
            asendus += i.lower()
                
        elif i.islower():
            asendus += i.upper()
        
        elif i.isspace(): 
            asendus += i
            
        elif i in string.punctuation:
            asendus += kirjavahemärk
            
    return asendus
          
    