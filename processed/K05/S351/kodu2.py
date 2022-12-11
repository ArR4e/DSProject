import random

def suurväike(sone):
    uus_sone=""
    #valib suvalise kirjavahemärgi, mida asendada
    suvaline_kirjavahemark=random.choice(['"',"'",".","?","!",",",":",";","-","(",")","{","}","[","]","/"])
    #muutused sõnes
    for taht in sone:
        #Suured tähed väikesteks
        if (taht.isupper())==True:
            uus_sone+=(taht.lower())
        #väikesed tähed suurteks
        elif (taht.islower())==True:
            uus_sone+=(taht.upper())
        #tühikud alles jätta
        elif (taht.isspace())==True:
            uus_sone+=taht
        #kirjavahemärgi asendamine suvalise kirjavahemärgiga
        elif taht in ('"',"'",".","?","!",",",":",";","-","(",")","{","}","[","]","/"):
            uus_sone+=suvaline_kirjavahemark
    return uus_sone

print(suurväike( '! ! " " ' ' ( ( ) ) , , - - . . / / : : ; ; ? ? [ [ ] ]'))