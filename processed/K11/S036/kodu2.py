def transponeeriK(m):
    arv = -1
    lisa = []
    for i in range(len(m[0])):
        vahe = []
        arv2 = -1
        for j in range(len(m)):
            
            vahe += [m[arv2][arv]]
            arv2 -= 1
        arv -= 1
        lisa +=[vahe]
    return lisa
print(transponeeriK([[],[]]))