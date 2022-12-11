import string
import random 

def suurväike(x):
    suva=random.choice(string.punctuation)
    asenda=x.maketrans(string.punctuation, suva*len(string.punctuation))
    x=x.translate(asenda)
    järjend=[]
    for i in x:
        if i.isupper():
            i=i.lower()
            järjend.append(i)
        else:
            i=i.upper()
            järjend.append(i)
    kokku="".join(järjend)
    return kokku
    
    


