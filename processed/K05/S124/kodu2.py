import string
import random
import re

def suurväike(sõne):
    l = ""
    i = 0
    uus_sümbol = random.choice('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    while i < len(sõne):
        sümbol = sõne[i]
        if sümbol.isalpha():
            if sümbol.isupper():
                sümbol = sümbol.lower()
            else:
                sümbol = sümbol.upper()
        elif sümbol in string.punctuation:
            sümbol = sümbol.replace(sümbol, uus_sümbol)
        i += 1
        l += sümbol
    return l
        
    
    

        

# def suurväike(sõne):
#     märk = random.choice('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
#     märgid = re.escape(string.punctuation)
#     tähed_vahetatud = sõne.swapcase()
#     uus_sõne = re.sub(r"["+märgid+"]", i, tähed_vahetatud)
#     return uus_sõne
# 
# suurväike('aAa,.')

#Kasutasin allpool olevalt saidil pakutud lahendust, [^a-zA-Z0-9 \n\.] ei läinud tööle, punktid jäid sisse.

#https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python
# import random
# import re
# import string
# 
# def suurväike(sõne):
#     vahetatud = sõne.swapcase()
#     result = string.punctuation
#     märk = ("".join(random.choice(result) for i in range(2)))
#     uus_sõne = re.sub('[^a-zA-Z0-9 \n\.]', märk, vahetatud)
#     #vahetatud.punctuation
#     return uus_sõne

# import re
# import string
# import random
# 
# def suurväike(sõne):
#     vahetatud = sõne.swapcase()
#     letters = string.punctuation
#     märk = random.choice(letters)
#     for i in vahetatud:
#         if i in string.punctuation:
#             uus_sõne = vahetatud.replace(i, märk)
#     return uus_sõne
#
#https://www.geeksforgeeks.org/string-punctuation-in-python/
# import re
# import string
# import random
# #print(string.punctuation)
# def suurväike(sõne):
#     vahetatud = sõne.swapcase()
#     letters = string.punctuation
#     l = random.choice(letters)
#     for i in vahetatud:
#         if i in string.punctuation:
#             l = random.choice(letters)
#     uus_sõne = vahetatud.replace(i, l)
#         #uus_sõne = re.sub(i, l, vahetatud)
#     #märk = (random.choice(letters) for i in range(2))
#     #uus_sõne = re.sub('[^a-zA-Z0-9 \n\.]', märk, vahetatud)
#     return uus_sõne
    
    