from random import randint

def suurväike(sisend):
    kirjavahemärgid='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    vastus = ("")
    rnd = randint(0,len(kirjavahemärgid))
    märk = kirjavahemärgid[rnd]             
    for el in sisend:
        if el.islower():
            vastus += el.upper()
        else:
            if el.isupper():
               vastus += el.lower()
            elif el in kirjavahemärgid:
                vastus +=märk
            else:
                vastus+=el
    return vastus
                
