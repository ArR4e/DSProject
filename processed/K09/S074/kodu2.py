from random import *
#List
minu_jarjend = [1, 3, 3, 4, 5, 5, 5, 6, 6]
#Shuffle funktsioon
def minu_shuffle(minu_jarjend):
    for el in range(len(minu_jarjend)):
        #Valib suvalise arvu vahemikus (0 - listi pikkus)
        shuffle = randint(0, len(minu_jarjend)-1)
        #Valib listist eelmises lauses genereeritud elemendi 
        uus = minu_jarjend[shuffle]
        #Vahetab ara listis olevate elementide kohad 
        minu_jarjend[shuffle] = minu_jarjend[el]
        #Numbrite vahetamine listis
        minu_jarjend[el] = uus

