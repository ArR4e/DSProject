import random

def suurväike(workstring):

    newstring = ""
    newconnector = random.choice('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    for letter in workstring:
        if(letter.isupper() and (letter.isalpha() or letter == " ")):
            newstring += letter.lower()
        elif(letter.islower) and (letter.isalpha()  or letter == " "):
            newstring += letter.upper()
        for i in ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
            if(letter == i):
                newstring += newconnector
                break
    return newstring