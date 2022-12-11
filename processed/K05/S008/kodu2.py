from random import randint
import string
sõne = input ("Sisestage oma tekst! ")

def suurväike (sõne):
    muutunudsõne = ""
    for täht in sõne:
        
        if täht.isupper():
           muutunudsõne += täht.lower()
           
        elif täht.islower():
            muutunudsõne += täht.upper()
            
        elif täht in string.punctuation:
            nr = randint (1, 3)
            
            if nr == 1:
                if täht != ",":
                    muutunudsõne += ","
                        
                else:
                    muutunudsõne += "&"
                
            elif nr == 2:
                if täht != "!":
                    muutunudsõne += "!"
                        
                else:
                    muutunudsõne += "?"
                        
            elif nr == 3:
                if täht != ":":
                    muutunudsõne += ":"
                        
                else:
                    muutunudsõne += "/"
                        
        else:
            muutunudsõne += täht
            
    return muutunudsõne
            
print (suurväike(sõne))