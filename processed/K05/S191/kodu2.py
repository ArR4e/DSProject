import random
import string   #mõlemat importi vaja kirjamärkide valiku jaoks

def suurväike(fraas):
    invert=""   #siia hakatakse lisama elemente
    märk=random.choice(string.punctuation)   #enne elementide kontrollimist valitakse suvaline märk mis teisi asendaks
    for i in fraas:   #iga elementi kontrollitakse eraldi
        if i.islower()==True:   #väikesed suureks
            invert+=i.upper()
        elif i.isupper()==True:   #suured väikeseks
            invert+=i.lower()
        elif i==" ":   #tühik jääb puutumata
            invert+=i
        else:    #märgid (praegusel juhul ka numbrid) asendatakse enne "for" tsüklit valitud märgiga
            i=märk
            invert+=i
    return invert