import string
import random

sõne = ""

def suurväike(sõne):
    random_kirjavahemärk = random.choice(string.punctuation)
    converted_sõne = ""
    
    for i in sõne:
        while(random_kirjavahemärk == i):
            random_kirjavahemärk = random.choice(string.punctuation)
            

    for i in sõne:
        if (i.isupper()):
            converted_sõne += (i.lower())
        elif (i.islower()):
            converted_sõne += (i.upper())
        elif (i.isspace()):
            converted_sõne += i
        elif (i in string.punctuation):
            converted_sõne += random_kirjavahemärk
            
    sõne = converted_sõne
    return(sõne)
        
