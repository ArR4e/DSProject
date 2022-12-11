from random import randint

def minu_shuffle(järjend):
    for i in range(len(järjend) * 5): #Siin võib kasutada mistahes range(väärtus)
        random_seed = randint(0, len(järjend) - 1)
        random_index = random_seed - randint(random_seed - len(järjend) + 1, random_seed)
        
        vahe_hoidla = järjend[random_seed]
        järjend[random_seed] = järjend[random_index]
        järjend[random_index] = vahe_hoidla