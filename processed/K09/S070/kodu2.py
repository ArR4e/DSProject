import random
def minu_shuffle(jada):
    järjekord = random.sample(range(len(jada)), (len(jada)))
    uusjada = []
    for i in range(len(jada)):
        uusjada.append(jada[järjekord[i]])
    for i in uusjada:
        jada.remove(jada[0])
        jada.append(i)