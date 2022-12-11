import string
import random
def split(word):
    return [char for char in word]
list=split(string.punctuation)
def suurväike(x):
    uus=x.swapcase()
    m2rk=random.choice(list)
    for i in uus:
        if i in list:
            uus=uus.replace(i,m2rk)
    return uus
sone=input("Sisestage sona voi lause:")
print (suurväike(sone))

            