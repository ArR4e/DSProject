##Kasutasin selle ülesandega interneti abi
##
##
import string
import random

algne = input("Sisesta lause: ")
uus = ""

for a in algne:
    if (a.isupper()) == True:
        uus += (a.lower())
        
    elif (a.islower()) == True:
        uus += (a.upper())
        
    elif (a.isspace()) == True:
        uus += a
    elif a in string.punctuation:
        uus += random.choice(string.punctuation)
        
print("Uus lause: ", uus)


