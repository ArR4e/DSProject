import random
def bingo():
    i = 0
    while i < 1:
        esimene_osa = random.sample(range(1,11), 3)
        teine_osa = random.sample(range(11,21),2)
        list = esimene_osa + teine_osa
        if 1 in list:
            if 2 in list:
                if 3 in list:
                    print("peab uue listi tegema")
        else:   
            return list
            i += 1