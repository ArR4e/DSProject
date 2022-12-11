import string
import re
from random import*
tagasi=0
a = ("mINA oled, SINA oled!?!")
def suurväike(a):
    tagastus = ""
    l = ""
    märgid = string.punctuation
    for täht in a:
        if täht == " ":
            tagastus += täht
            continue
            
        suvaline = randint(0, 32)
        k = 0
        if täht in märgid:
            for x in märgid:
                if suvaline == k:
                    l = x
                    break
                k += 1
            tagastus += l
            continue
        if re.search("[a-z]", täht): #https://www.geeksforgeeks.org/python-program-check-validity-password/
            tagastus += täht.upper()
            continue
        elif re.search("[A-Z]", täht):
            tagastus += täht.lower()
            continue
    return(tagastus)
print(suurväike(a))