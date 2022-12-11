#https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
def transponeeriK(maatriks):
    t = []
    a = []
    for el in maatriks:
        l = len(maatriks) - 1
        p = len(el) - 1
    for i in range(p, -1, -1):
       a = []
       for j in range(l, -1, -1):
           a += [maatriks[j][i]]
       t += [a]
    return t
           




#print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

