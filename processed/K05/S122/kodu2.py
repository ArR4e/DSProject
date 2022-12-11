import random
import string
def suurväike(sõne):
    vahetatud_sõne = ""
    vahetusmärgid = ['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]
    vahetusmärk = random.choice(vahetusmärgid)
    for täht in sõne:
        if täht.islower() == True or täht.isupper() == True:
            vahetatud_täht = täht.swapcase()
            vahetatud_sõne = vahetatud_sõne + vahetatud_täht
        elif täht == " ":
            vahetatud_sõne = vahetatud_sõne + " "                       
        elif täht in string.punctuation:
            vahetatud_sõne = vahetatud_sõne + vahetusmärk
    return vahetatud_sõne
