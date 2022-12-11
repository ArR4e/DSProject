import string
import random

def suurväike(sone):
    c = ""
    
    p = random.choice(string.punctuation)
    
    for element in string.punctuation:
        sone = sone.replace(element, p)
         
    for element in sone:
        if element == element.upper():
            a = element.lower()
            b = element.replace(element, a)
            c = c + b
        elif element == element.lower():
            a = element.upper()
            b = element.replace(element, a)
            c = c + b

         
         
            
            
    return c
        
print(suurväike("!ToRT"))   
    