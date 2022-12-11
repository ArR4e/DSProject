from random import sample
def bingo():
    järjend = []
    while True:
        esimene = sample(range(1,11), 3)
        if 1 in esimene and 2 in esimene:
            esimene = sample(range(1,11), 3)
        else:
            break
    teinekolmas = sample(range(11, 21), 2)
    järjend = esimene + teinekolmas
    return(järjend)