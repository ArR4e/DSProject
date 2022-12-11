import random
def suurväike (sona):
    uus=""
    a=random.randint(1,3)
    if a<=1:
        l="!"
    elif a==2:
        l="%"
    elif a==3:
        l="?"
    for i in range (len(sona)):
        
        if sona[i].isupper():
            uus+=sona[i].lower()
        elif sona[i].islower():
            uus+=sona[i].upper()
        elif sona[i]==" ":
            uus+=" "
        else:   
            uus+=l
    return uus

