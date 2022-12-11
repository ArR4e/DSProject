from random import randint

järjend = [1, 3, 3, 4, 5, 5, 5, 6, 6]

def minu_shuffle(järjend):
    for s in range(len(järjend) - 1, 0, -1):
        juhuslik_arv = randint(0, s)
        järjend[s], järjend[juhuslik_arv] = järjend[juhuslik_arv], järjend[s]
    
print(minu_shuffle(järjend)) 
   
    
    
    
