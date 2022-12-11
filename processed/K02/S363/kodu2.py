# N on lambipostide arv
# s on maksimaalne vahemaa (täisarv)
# m on liini pikkus (täisarv meetrites)

m = int(input("Palun sisesta liini pikkus: "))
s = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus: "))

if m%s==0:
    N=int((m/s)+1)
    
if m%s!=0:
    N=int((m/s)+2)
    
print(N)