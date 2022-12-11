import string
import random
a = input("Sisestage sõna: ")

def suurväike(a):
    uussõna = ""
    kirjavahemärgid = []
    for j in string.punctuation:
        kirjavahemärgid.append(j)
    suvalinemärk = random.choice(kirjavahemärgid)
    for i in range(len(a)):
        if a[i].isupper():
            uussõna = uussõna + a[i].lower()
        elif a[i].islower():
            uussõna = uussõna + a[i].upper()
        elif a[i] in kirjavahemärgid:
            uussõna = uussõna + suvalinemärk
        else:
            uussõna = uussõna + a[i]
    return uussõna
print(suurväike(a))