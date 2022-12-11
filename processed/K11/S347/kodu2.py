def transponeeriK(maatriks):
    järjend =[]
    ridadearv= len(maatriks)-1
    veergudearv = len(maatriks[0])-1
    for i in range(veergudearv, -1, -1):
        järjend2 = []
        for j in range(ridadearv, -1, -1):
            a =maatriks[j][i]
            järjend2.append(a)
        järjend.append(järjend2)
    return järjend
    
print(transponeeriK([[1,2,3,4],[2,3,4,4],[3,3,3,4],[1,2,3,4]]))
        