
def transponeeriK(maatriks):
    transponeeritud = []
    ridade_arv = 0
    veergude_arv = 0
    for rida in maatriks:
        ridade_arv += 1
        for element in rida:
            veergude_arv += 1
    õige_veergude_arv = int(veergude_arv/ridade_arv)
    õige = []
    
    for i in range(õige_veergude_arv-1,-1,-1):
        tühi = []
        for j in range(ridade_arv-1,-1,-1):
            tühi += [maatriks[j][i]]
        transponeeritud += [tühi]
    return(transponeeritud)

print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transponeeriK([[4, 31, 67, 99]]))

