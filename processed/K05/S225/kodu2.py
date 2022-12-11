from random import *
import string
def suurväike(a):
    b = ''
    y = ''.join(choices(string.punctuation))
    for x in a:
        if x.isupper() == True:
            b += x.lower()
        elif x.islower() == True:
            b += x.upper()
        elif x.isspace() == True:
            b += x
        elif x in string.punctuation:
            b += y
    return b
    
# a = input('Lause: ')
# 
# print(suurväike(a))