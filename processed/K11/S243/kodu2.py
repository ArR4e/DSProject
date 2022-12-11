#maatriksi transponeerimine kõrvaldiagonaali järgi

def transponeeriK(maatriks):
    ridu=len(maatriks)
    veerge=len(maatriks[0])
    transponeeritud=[]
    for u in range(veerge):
        i=u+1
        veerg=[]
        for rida in maatriks:
            veerg.append(rida[-i])
        if veerge !=1 or ridu !=1:
            ümberkeeratud_veerg=[]
            for element in veerg:
                indeks=veerg.index(element)+1
                ümberkeeratud_veerg.append(veerg[-indeks])
            veerg=ümberkeeratud_veerg
        transponeeritud.append(veerg)
    return transponeeritud
    
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]] #[[9, 6, 3], [8, 5, 2], [7, 4, 1]]
B=[[1, 2], [3, 4], [5, 6], [7, 8]] #[[8, 6, 4, 2], [7, 5, 3, 1]]
C=[[4, 31, 67, 99]]#[[99], [67], [31], [4]]
D=[[1], [2], [3], [4], [5]]

print(transponeeriK(A))
print(transponeeriK(B))
print(transponeeriK(C))
print(transponeeriK(D))