from random import randint

def minu_shuffle(järjend):
#muutma peab olemasolevat listi, mitte uut tegema
    
    for i in range(len(järjend)**2):
        a = järjend.pop(randint(0,len(järjend)-1))
        järjend.insert(len(järjend),a)
    
    

