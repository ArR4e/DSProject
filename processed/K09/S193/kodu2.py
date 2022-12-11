#randit 

import random

#random_järjend = [1, 8, 5, 9, 7]

def minu_shuffle(järjend):
    for i in range(len(järjend)-1, 0, -1):
        j = random.randint (0, i + 1)  #valime randomselt indexit 0-st 1-ni
        järjend[i], järjend[j] =  järjend[j], järjend[i]
    #return järjend
    
#print ("Järjend elementidega juhuslikus järjekorras: " + str(my_shiffle(random_järjend)))
    