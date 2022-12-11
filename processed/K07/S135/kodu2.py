teepikkus = float(input("sisestage teepikkus kilomeetrites "))
f = open("taksohinnad.txt", encoding = "UTF-8")
odavaimTakso = ""
odavaimTaksoHind = 0
for takso in f:
    taksoList = takso.split(",")
    hind = float(taksoList[1]) + teepikkus * float(taksoList[2])
    if odavaimTaksoHind > hind or odavaimTaksoHind == 0:
        odavaimTaksoHind = hind
        odavaimTakso = taksoList[0]
        continue
    
print("Odavaim takso on", odavaimTakso)
