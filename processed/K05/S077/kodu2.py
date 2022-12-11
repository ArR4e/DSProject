from string import punctuation
from random import choice 

def suurväike(sõne):
    a=sõne.swapcase()
    for i in a:
        if i in punctuation:
            a=a.replace(i,".") 
    a=a.replace(".",choice(punctuation)) #suvaline kirjavahemärk https://www.codegrepper.com/code-examples/python/what+does+random.choice+%28string.punctuation%29+and+how+do+I+generate+a+hash
    return a

