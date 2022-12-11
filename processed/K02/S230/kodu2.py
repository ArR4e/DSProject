from math import ceil
liin=int(input("Sisestage liini pikkus meetrites: "))
max=int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
poste=ceil(liin /max+1)
print("Liini ehitamiseks on vaja vähemalt",poste ,"posti.")