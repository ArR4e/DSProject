import random
import string

def suurväike (a):
    vahetus = []
    b = random.choice(string.punctuation) #Valin suvalise sümboli, millega kõiki stringis olevaid kirjavahemärke asendada
    vastus = ''
    symbol = set(string.punctuation)
    for i in a:
        if i == ' ':
            vahetus.append(' ')
        elif i.isupper():
            vahetus.append(i.lower())
        elif i.islower():
            vahetus.append(i.upper())
        elif any(s in symbol for s in i): #Asendan kõik kirjavahemärgid eelnevalt defineeritud suvalise sümboliga b
            vahetus.append(b)
            
    return vastus.join(vahetus) 