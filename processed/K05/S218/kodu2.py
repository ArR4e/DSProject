import string
import random

def suurväike(sõne):
    c = random.choice(string.punctuation)
    uus = ""
    for i in range (len(a)):
        if a[i].isupper():
            uus = uus + a[i].lower()
        elif a[i].islower():
            uus = uus + a[i].upper()
        if a[i] in string.punctuation:
            uus = uus + a[i].replace(a[i], c)
        if a[i].isspace() == True:
            uus = uus + " "
    return uus
 
            
a = input("Sisesta mingi sõne: ")
print(suurväike(a))





    

    
        
    