import string
import random
string.punctuation = '!#"$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punctuation = random.choice('!#"$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
def suurväike(x):
    x = x.replace(string.punctuation, punctuation)
    return str.swapcase(x)