from random import randint
import string

mark = []

for i in string.punctuation:
    mark.append(i)
    
def suurväike(x):
    
    nr = randint(0, (len(mark) - 1))
    uus = ""
    
    for taht in x:
        
        if taht.isupper():
            uus += taht.lower()
            
        elif taht.islower():
            uus += taht.upper()
            
        elif taht == " ":
            uus += " "
            
        else:
            uus += mark[nr]
            
    return uus
        
        
            