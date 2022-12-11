import string
from random import randint

margid=[]
for i in string.punctuation:
    margid.append(i)

def suurväike(sone):
    uussone=''
    jarjekorranr=randint(0,(len(margid)-1))
    for taht in sone:
        if taht.isupper():
            uussone+=taht.lower()
        elif taht.islower():
            uussone+=taht.upper()
        elif taht==' ':
            uussone+=' '
        else:
            uussone+=margid[jarjekorranr]
    return uussone


