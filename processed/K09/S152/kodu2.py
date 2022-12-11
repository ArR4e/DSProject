import random
def minu_shuffle(järjend):
    n = len(järjend)
    for i in range(0, n-1,2):
        järjend[i], järjend[i+1] = järjend[i+1], järjend[i]
    #return(järjend)
        
        
