import random
järjend = []
def minu_shuffle(järjend):
    a = 0
    uus = []
    while len(järjend)!=a:
        b = random.choice(järjend)
        järjend.pop(järjend.index(b))
        järjend.append(b)
        a = a + 1
    #return (järjend)
minu_shuffle(järjend)

        



        

