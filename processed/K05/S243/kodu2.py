#Suured väikeseks, väikesed suureks
import random
import string

def suurväike(sõne):
    uus_sõne=""
    märgid=''.join(random.choices(string.punctuation, k=1))
    for letter in sõne:
        a=letter
        if a == " ":
            uus_sõne+=a
        if a in string.punctuation:
            a=str(märgid)
            uus_sõne+=a
        if a.isupper():
            uus_sõne+=a.lower()
        if a.islower():
            uus_sõne+=a.upper()
    return uus_sõne
            
#string.punctuation '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'