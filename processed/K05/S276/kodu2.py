import string
import random
def suurväike(x):
    a=random.choice(string.punctuation)
    lause=""
    for i in x:
        if i.isupper() == True:
            lause += i.lower()
        elif i.islower() == True:
            lause += i.upper()
        elif i in string.punctuation:
            lause += a
        elif i == " ":
            lause += " "
    print(lause)