from math import ceil
def sisend():
    liinipikkus = int(input("Liini pikkus meetrites: "))
    postidekaugus = int(input("Maksimaalne postide vaheline kaugus meetrites: "))
    return(liinipikkus,postidekaugus)

pikkused = []
sisendtuple = sisend()
pikkused.append(sisendtuple[0])
pikkused.append(ceil(sisendtuple[1]))

while pikkused[0] <= 0 or pikkused[1] <= 0:
    print("Ebasobiv sisend.")
    pikkused = []
    sisendtuple = sisend()
    pikkused.append(sisendtuple[0])
    pikkused.append(sisendtuple[1])

postidearv = 0

muutuja = pikkused[0]
if pikkused[0]/pikkused[1] > 1:
    if pikkused[1] == 1:
        postidearv = pikkused[0]+1
    while muutuja > 0:
        if pikkused[0]/muutuja > ceil(pikkused[0]/pikkused[1]):
            postidearv = ceil(pikkused[0]/muutuja)
            muutuja = 0
        else:
            muutuja -= 1
else:
    postidearv = 2
    
    
print(int(postidearv), "posti")
    