def suurväike(x):
    if x.isalnum():
        return x.swapcase()
    else:
        y = random.choice('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        sõna = re.sub ('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', y, x)
        return sõna.swapcase()
       
       
import random
import re

    