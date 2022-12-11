import string
from random import *

def suurväike(text):
    muudetud=""
    suvaline=string.punctuation[randint(0,len(string.punctuation)-1)]
    for char in text:
        #Kui suur täht,teeb väikeseks
        if char.isupper():
            muudetud += char.lower()
        #Kui väike täht, teeb suureks
        elif char.islower():
            muudetud += char.upper()
        #Vaatab kas punctuationites on sümbol olemas. Kui jah, siis muudab selle suvaliseks punctuationiks
        elif string.punctuation.find(char) != -1:
            muudetud += suvaline
        else:
            muudetud += char
    return muudetud