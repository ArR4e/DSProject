import string
import random
def suurväike(tekst):
    sümbol = random.choice(string.punctuation)
    sõna = ""
    for i in tekst:
        if i not in string.punctuation:
            sõna += i
        else:
            sõna += sümbol
          

    suurjaväike = sõna.swapcase()
 
    return(suurjaväike) 

suurväike(input("Sisestage tekst: "))
    
    