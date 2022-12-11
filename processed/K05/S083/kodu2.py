import re
import random
import string

def suurväike(sõne):
    uus_märk = random.choice(string.punctuation)
    uus_sõne = re.sub('[^a-zA-Z0-9öÖäÄüÜõÕ \n]', uus_märk, sõne).swapcase()
    return uus_sõne      
    
    
sõne=input('Sisesta sõna: ')
print(suurväike(sõne))
