import math
print("Palun, sisestage admeid ainult täisarvuna meetrites")
linni_pikkust = int(input("Sisestage liini pikkust: "))
maxkaugust = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugust: "))
print("Liini ehitamiseks minimaalselt vaja:", math.ceil(linni_pikkust / maxkaugust + 1))
