import string
import random

def suurväike(sõne):
    
    uus=""
    kirjavahemärk=random.choice(string.punctuation)
    for i in range (len(sõne)):
        if sõne[i].isupper():
            uus+=sõne[i].lower()
            
        elif sõne[i].islower():
            uus+=sõne[i].upper()
            
        elif sõne[i] in string.punctuation:
            uus+=kirjavahemärk
           
        else:
            uus+=sõne[i]
        
    return uus
            
sõne=input("Sisesta sõne:")

print(suurväike(sõne))
            

    
    
    


        