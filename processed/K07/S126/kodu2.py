#andmete saamine
a = float(input("Sisesta tee pikkus kilomeetrites: "))
#faili avamine
f = open('taksohinnad.txt', 'r')
odavaim_takso = " "
odavaim_hind = 0 
#failist lugemine
for rida in f:
    arve = rida[0] 
    r = rida.split(",")
    arve = float(r[1]) + float(r[2]) * a
    print(arve)
    
    if arve < odavaim_hind:
        odavaim_hind = arve
        
        odavaim_tasko = rida[0]
print("Kõige odavam on ", odavaim_takso)
f.close()