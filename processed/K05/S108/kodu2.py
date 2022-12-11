import random
import string

def suurväike(sõne):
    uus=""
    tähed=sõne.strip(string.punctuation)
    märgid=sõne.replace(tähed, "")
    tähed.swapcase()
    kirjavahemärk=random.choice(string.punctuation)
    for i in range (len(märgid)):
        if märgid[i] in string.punctuation:
            uus+=kirjavahemärk
    
    return tähed+uus
    
sõne=input("Sisesta mingi sõne: ")
print(suurväike(sõne))

    