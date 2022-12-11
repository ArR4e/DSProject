from math import *

pikkus=int(input('Sisesta elektriliini pikkus täisarv meetrites: '))

vahe=int(input('Sisesta kahe posti vaheline maksimaalkaugus täisarv meetrites: '))

x=ceil(pikkus/vahe)+1

print('Elektriliini ehitamiseks on minimaalselt vaja',x,'posti.')