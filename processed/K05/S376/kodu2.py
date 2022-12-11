import string
import random

def suurväike(sõne):
    uussõne = ""
    kirjavahemärgid = string.punctuation
    kirjavahemärk = random.choice(kirjavahemärgid)

    for sümbol in sõne:
        
        if sümbol.isupper():
            uussõne += sümbol.lower()
        
        if sümbol.islower():
            uussõne += sümbol.upper()
            
        if sümbol in kirjavahemärgid:
            uussõne += kirjavahemärk
        
        if sümbol == " ":
            uussõne += " "
        
    return uussõne