from random import randint

def minu_shuffle(järjend):
    indeksid = []
    uus_järjend = []
    for el in järjend:
        indeks = randint(0, len(järjend)-1)
        while indeks in indeksid:
            indeks = randint(0, len(järjend)-1)
        indeksid.append(indeks)
        uus_järjend.append(järjend[indeks])
    järjend.clear()
    for element in uus_järjend:
        järjend.append(element)


#a = [1,2,3,4,5,6]
#minu_shuffle(a)
#print(a)