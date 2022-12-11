f = open("taksohinnad.txt", "r", encoding = "UTF-8")

teepikkus = float(input("Sisestage kodutee pikkus kilomeetrites: "))
parim_hind = float('inf')
sõna = ""
listiks = []
parim_firma = ""

while True:
    rida = f.readline().strip("\n") + ","
    if rida == ",":
        break
    
    for i in rida:
        if i == ",":
            listiks.append(sõna)
            sõna = ""
            continue
        sõna += i
        
    hind = float(listiks[1]) + teepikkus * float(listiks[2])
    
    if hind < parim_hind:
        parim_hind = hind
        parim_firma = listiks[0]
        
    listiks = []
    
f.close()

print("Kõige odavam on " + parim_firma)