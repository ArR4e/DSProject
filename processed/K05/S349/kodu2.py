import string
import random
def suurväike(sõne):
    for i in sõne:
        if i in string.punctuation:
            i = i.replace(i, random.choice(string.punctuation))
            sõne.swapcase()
        
       
           

suurväike("OoN?")

????????? ei oska kahjuks edasi 