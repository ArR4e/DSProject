import copy
def transponeeriK(maatriks):
    järjend=[]
    veergude_arv = len(maatriks[0])
    indeks=0
    for i in range(veergude_arv-1,-1,-1):
        järjend.append([])
        for j in range(len(maatriks)-1,-1,-1):
            järjend[indeks].append(maatriks[j][i])
        indeks+=1
    return järjend



print(transponeeriK([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]))