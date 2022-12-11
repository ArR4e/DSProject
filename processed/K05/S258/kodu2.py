
import string
import random
gei= "qwertyuiopüõasdfghjklöäzxcvbnm"
GEI= gei.upper()
def suurväike(MEGA):
    rando = random.randint(0,len(string.punctuation)-1)
    jupiter=""
    global gei
    global GEI
    for i in MEGA:
        if i in gei:
            jupiter+=i.upper()
        elif i in GEI:
            jupiter+= i.lower()
        elif i == " ":
            jupiter+=i
        elif i in string.punctuation:
            jupiter+=string.punctuation[rando]
    return jupiter

