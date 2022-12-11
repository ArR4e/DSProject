f = open("taksohinnad.txt", "r")
teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))
odavaim = 0
for line in f.readlines():
    jarjend = line.rstrip().split(',')
    hind = float(jarjend[1]) + (teepikkus*float(jarjend[2]))
    if hind < odavaim or odavaim == 0:
        odavaim = hind
        odavaimtakso = jarjend
f.close()

print("Kõige odavam on", odavaimtakso[0]+".")      
    
        


    