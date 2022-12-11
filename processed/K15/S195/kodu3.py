def bussif(bussid):
    sobivad = []
    saabumine = '16:30'
    lahkumine = '09:00'
    hind = '5'
    for buss in bussid:
        sobib = True
        if buss[2] <= hind:
            hind = buss[2]
            sobib = True
        else:
            sobib = False
        if sobib:
            sobivad.append(buss)
            
    return sobivad


bussid = []

failinimi = str(input("Palun sisestage failinimi: "))

f = open(failinimi,"r")


while True:
    x = f.readline().strip("\n")
    if x == "":
        break
    x = x.split()
    bussid.append(x)
    
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")

for buss in bussif(bussid):
    print(buss[0],buss[1],buss[2])
    
 
f.close()