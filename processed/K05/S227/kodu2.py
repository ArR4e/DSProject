import string
import random
L=random.choice(string.punctuation)
def suurväike(x):
    newstring=""
    for i in x:
        if i.isupper() == True:
            newstring+=i.lower()
        elif i.isspace()==True:
            newstring+=i
        elif i.islower() ==True:
            newstring+=i.upper()
        elif i in string.punctuation:
            newstring+=L
    return newstring

        
        
