from random import sample #Kattumatute juhuslike arvude genereerimiseks

def bingo():
    numbrid = []
    proov = []
    while True:
        proov = sample(range(1,11),3)
        üks = ""
        kaks = ""
        kolm = ""
        for i in proov:
            if i == 1:
                üks = True
            elif i == 2:
                kaks = True
            elif i == 3:
                kolm = True
                
        if üks != kaks or kaks != kolm or kolm != üks:
            numbrid.append(proov)
            break
            
    numbrid.append(sample(range(11,21),2))
    vastus =[]
    for kast in numbrid:
        for arv in kast:
            vastus.append(arv)
    return vastus

print(bingo())