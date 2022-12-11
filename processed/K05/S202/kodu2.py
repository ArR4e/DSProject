import string
import random

def listmaker(makee):
    list1 = []
    list1[:0] = makee
    return list1
#listi tegija https://www.geeksforgeeks.org/python-program-convert-string-list/

muut = listmaker(string.punctuation)
def suurväike(alg):
    suurused = alg.swapcase()
    juh = random.choice(string.punctuation)
    sv = suurused
    for i in muut:
            sv = sv.replace(i, juh)
#modifiesin siit saadud loopi https://www.kite.com/python/answers/how-to-replace-multiple-characters-in-a-string-in-python
    return sv

