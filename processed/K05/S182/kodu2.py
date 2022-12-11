import random
import string
def suurväike(sõne):
    a=0
    c=random.choice(string.punctuation)
    while len(sõne)>a:
        sõne[a]
        if sõne[a]==" ":
            print(" ",end="")
        elif bool(sõne[a]==sõne[a].upper()==sõne[a].lower())==True:
            print(c,end="")
        
        elif bool(sõne[a]==sõne[a].upper())==True:
            print(sõne[a].lower(),end="")
        elif bool(sõne[a]==sõne[a].lower())==True:
            print(sõne[a].upper(),end="")
        a+=1   
            
suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")