import random

def suurväike (sõne):
    for sümbol in sõne:
        if sümbol == sümbol.lower():
            uus = sümbol.upper()
        elif sümbol == sümbol.upper():
            uus = sümbol.lower()
        else:
            uus = random.choince(punctuation)
        print(uus)
        
#tean, et see ei tööta nii, nagu peab, aga praegu ei ole rohkem ideeid :(