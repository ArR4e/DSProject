#def suurväike():
import string
import random
b = "MinA oleN Tubli!!"
#b= string.punctuation
#print(b)

#esimese punktuatsiooni võtab
def suvalinepunkts():
    for i1 in b:
        s1 = str(i1)
        l1 = "0"
        if s1 in string.punctuation:
            l1 = random.choice(string.punctuation)
        if s1 in string.punctuation:
            break
    return l1
#püsiv muutuja esimese punktuatsiooni suhtes
o = str(suvalinepunkts())
 

def suurväike(a):
    list = []
    for i in a:
        s = str(i)
        m = s
        l = "0"
        if s == s.upper():
            l = m.lower()
        if s == s.lower():
            l = m.upper()
        if s in string.punctuation:
#on võimalik kontrollida kas täht stringis on seotud punktuatsiooni väärtusega. Ehk kas langeb kokku (char)-iga, see on pythonisse sisse installeeritud folderis "string".
            l = o
#random.choice sisse installeeritud programm võtab/valib char-ist ühe väärtuse
        list.append(l)

    j = "".join(list)
    return j
print(suurväike(b))