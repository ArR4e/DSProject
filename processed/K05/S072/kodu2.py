from random import choice
import string

def suurväike(sõne):
    väljund = []
    juhuslik_sümbol = choice(string.punctuation)
    
    for täht in sõne:
        if täht == ' ' or täht.isdigit():
            väljund.append(täht)
        elif täht.isalpha():
            väljund.append(täht.upper() if täht.islower() else täht.lower())
        else:
            väljund.append(juhuslik_sümbol)
            
    return ''.join(väljund)            