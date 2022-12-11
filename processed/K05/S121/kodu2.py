import string
import random
import re

def suurväike(s):
    new_s = s.swapcase()
    punct = string.punctuation
    list1 = list(punct)
    rand = random.choice(list1)
    new_text = re.sub(r'[^\w\s]',rand, new_s)
    return new_text
    
print(suurväike("sdhfushoIUGUIGb!"))
