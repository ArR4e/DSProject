#Suured väikesteks ja väikesed suurteks
import random
import string

sümbolid = string.punctuation
suvaline = random.choice(sümbolid)

def suurväike(sõne):
    vahetatud = sõne.replace(sümbolid, suvaline).swapcase()
    print(vahetatud)