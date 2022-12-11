import random
def minu_shuffle(järjend):
    for i in range((len(järjend) - 1)):
        suva_arv = random.randint(0, len(järjend)-1)
        järjend[i], järjend[suva_arv] = järjend[suva_arv], järjend[i]
    return(järjend)

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

#print(len(a))
