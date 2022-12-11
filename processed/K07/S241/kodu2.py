fail = open("taksohinnad.txt", encoding="UTF-8")
km=float(input("Sisesta tee pikkus kilomeetrites: "))
i=1
kulu =[]
firma = []
for i in range(3):
    a=fail.readline().strip().split(",")
    sõidukulu = float(a[1]) + float(a[2])*km
    kulu.append(sõidukulu)
    firma.append(a[0])
if (kulu[0] < kulu[1] and kulu[0] < kulu[2]):
    b=0
elif (kulu[0] > kulu[1] and kulu[1] < kulu[2]):
    b=1
else:
    b=2
print("Kõige odavam on", firma[b])        
fail.close()
