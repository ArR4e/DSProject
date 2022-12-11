teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")

hind=[]
firma=[]
for rida in f:
    reajärjend = rida.split(",")
    hind.append(float(reajärjend[1]) + float(reajärjend[2]) * teepikkus)
    firma.append(reajärjend[0])
try:
    print(f"Kõige odavam on ", firma[hind.index(min(hind))])
except:
    print("Fail on tühi")
        
    
        
        
