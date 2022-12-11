import random
import string

def suurväike():
    sõne = input("Sisesta lause:")
    uussõne = ""
    suur = 0
    väike = 0
    märk = 0
    uusmärk = random.choice(string.punctuation)
    for a in sõne:
        if (a.isupper()) == True:
            suur += 1
            uussõne +=(a.lower())
        elif (a.islower()) == True:
            väike += 1
            uussõne += (a.upper())
        else:
            märk += 1
            uussõne += uusmärk
    print(uussõne)
        
 



suurväike()