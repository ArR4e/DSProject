from random import randint
def minu_shuffle(arvud):
    if len(arvud)==1:
        arvud=arvud
    else:
        for i in range(len(arvud)):
            arvud.append(arvud.pop(randint(0,len(arvud)-i-1)))
    arvud=arvud
a = [22, 22, 22, 22, 22]
minu_shuffle(a)
print(a)