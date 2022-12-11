teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding = 'UTF-8')

takso1 = f.readline().strip().split(",")
takso2 = f.readline().strip().split(",")
takso3 = f.readline().strip().split(",")

hind1 = float(takso1[1]) + float(takso1[2]) * teepikkus
hind2 = float(takso2[1]) + float(takso2[2]) * teepikkus
hind3 = float(takso3[1]) + float(takso3[2]) * teepikkus
if hind1 < hind2 and hind1 < hind3:
    print("Kõige odavam on", takso1[0] + ".")
elif hind2 < hind1 and hind2 < hind3:
    print("Kõige odavam on", takso2[0] + ".")
else:
    print("Kõige odavam on", takso3[0] + ".")
f.close()