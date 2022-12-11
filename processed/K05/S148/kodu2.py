def suurväike(a):
    import string
    import random
    uus = ""
    sümbol = string.punctuation
    uus_sümbol = random.choice(sümbol)
    
    for b in a:
        if b.islower() == True:
            uus += b.upper()
        elif b.isupper() == True:
            uus += b.lower()
        elif b in string.punctuation:
            uus += uus_sümbol
        elif b == " ":
            uus += " "
    return uus