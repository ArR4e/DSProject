import math

pikkus=int(input('Sisestage liini pikkus meetrites: '))
kaugus=int(input('Sisestage postide maksimaalkaugus meetrites: '))
if pikkus%kaugus==0:
    posti_arv=pikkus/kaugus+1
elif pikkus%kaugus!=0:
    posti_arv=math.ceil(pikkus/kaugus)+1
elif pikkus<=kaugus:
    posti_arv=2
    
print(int(posti_arv))