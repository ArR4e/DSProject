from random import randint

#def minu_shuffle(järjend):
 #   vahetatud=random.sample(järjend,len(järjend))
  #  return vahetatud
  
def minu_shuffle(järjend):
    if len(järjend)!=0 and len(järjend)!=1:
        for el in järjend:
            pikkus = len(järjend)
            indeks = järjend.index(el)
            uus = randint(0,pikkus-1)
            järjend[indeks]=järjend[uus]
            järjend[uus]=el
        
    
