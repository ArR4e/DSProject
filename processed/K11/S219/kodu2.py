def transponeeriK(maatriks):
    abilist = []
    ridade_arv = len(maatriks)
    tulpade_arv = len(maatriks[0])
    for i in range(tulpade_arv):
        tulp = [rida[tulpade_arv-1] for rida in maatriks]
        tulp.reverse()
        abilist.append(tulp)
        if tulpade_arv > 1:
            tulpade_arv -= 1
        else:
            break
    return abilist
    
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))