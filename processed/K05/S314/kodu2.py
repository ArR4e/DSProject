import string 
import random 
def suurväike(sõne):
    väljund = ""
    sym = random.choice(string.punctuation)
    for täht in sõne:
        if täht.isupper():
            väljund += täht.lower()
        elif täht.islower():
            väljund += täht.upper()
        elif täht == " ":
            väljund += " "
        else:
            väljund += sym
    return väljund
            

a = input("Sisesta sõne: ")

print(suurväike(a))