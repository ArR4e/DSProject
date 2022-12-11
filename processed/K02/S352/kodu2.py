from math import*
liin=int(input("Sisestage elektriliini pikkus: "))
postide_k=(int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: ")))
poste=ceil(liin/postide_k+1)

print(liin,"m pikkuse liini ehituseks on vaja minimaalselt ", poste, " posti")