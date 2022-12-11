import string
import random
def suurväike(lause):
    i = 0
    ulause = ""
    rand = random.randint(0,len(string.punctuation))
    while i < len(lause):
        if lause[i] == " ":
            ulause = ulause + " "
        if lause[i] in string.punctuation:
            ulause = ulause + string.punctuation[rand]
        elif lause[i].isupper():
            ulause = ulause + lause[i].lower()
        else:
            ulause = ulause + lause[i].upper()
        i+=1
    return ulause         
