f = open("taksohinnad.txt" , "r")
tee_pikkus = float((input("Sisestage tee pikkus kilomeetrites: ")))
odavaimtakso = ""
odavaimhind = 1000000
for rida in f: 
    a = rida.strip().split(",")
    if (float(a[1]) + float(a[2])*tee_pikkus) < odavaimhind:
        odavaimtakso = a[0]
        odavaimhind = (float(a[1]) + float(a[2])*tee_pikkus)
print(odavaimtakso)

