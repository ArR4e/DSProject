import math
a= int(input("Sisesta rajatava trassi pikkus: "))
b= int(input("Sisesta kõrvuti asetsevate postide maksimaalkaugus: "))
c=math.ceil((a/b)+1)
print("Liini ehitamiseks on minimaalselt vaja " + str(c)+ " posti")