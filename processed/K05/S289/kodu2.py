import string
import random
def suurväike(a):
    s = ''
    x = random.choice(string.punctuation)
    for i in a:
        if i == i.upper() and not i in string.punctuation:
            s += i.replace(i, i.lower())
        elif i == i.lower() and not i in string.punctuation:
            s += i.replace(i, i.upper())
        elif i in string.punctuation:
            s += i.replace(i, x)
        elif i == " ":
            s += " "
    return s
        
a = ('! ! " " ' ' ( ( ) ) , , - - . . / / : : ; ; ? ? [ [ ] ]')
print(suurväike(a))
