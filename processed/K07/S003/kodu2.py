teepikkus = float(input("Palun sisesta teepikkus koju kilomeetrites: "))
f = open("taksohinnad.txt")
odavaimhind = 0
odavaimtakso = "0"
for line in f:
    takso = line.strip("\n").split(",")
    taksohind = float(takso[1]) + (teepikkus * float(takso[2]))
    if taksohind < odavaimhind or odavaimhind == 0:
        odavaimhind = taksohind
        odavaimtakso = takso
f.close()
    
print("Kõige odavam on " + odavaimtakso[0])