# 2. Suured väikseks ja väiksed suureks (5. kodutöö)

import random
import string

def suurväike(sõne):
    sümbol = random.choice(string.punctuation)
    sõne_uus = ""
    while True:
        for i in range(len(sõne)):
            if sõne[i].isupper():
                sõne_uus += sõne[i].lower()
            elif sõne[i].islower():
                sõne_uus += sõne[i].upper()
            elif sõne[i] == "":
                sõne_uus += sõne[i]
            else:
                for b in string.punctuation:
                    sõne_uus += sõne[i].replace(sõne[i], sümbol)
                    break
        return sõne_uus
    
print(suurväike("Õues paistab päike, sajab vihma."))        