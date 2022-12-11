import random
import string

kirjavahemärgid = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''

def suurväike(sõne):
    muutus= random.choice(kirjavahemärgid)
    for i in sõne:
        if i in string.punctuation:
            sõne = sõne.replace(i, muutus)
                #print(kirjavahe)
    sõne = sõne.swapcase()
    return sõne
    

#print(suurväike("Ma' ei taha, seda teha"))
    
    
    
#suur ja väiketähe vahetus - https://www.programiz.com/python-programming/methods/string/swapcase    