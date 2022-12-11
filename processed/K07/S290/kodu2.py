tee_pikkus=float(input("Sisesta tee pikkus kilomeetrites: "))

f=open("taksohinnad.txt")
taksode_hinnad=[]
nimed=[]

for rida in f:
    rida= rida.split(',')
    taksonimi = rida[0]
    nimed.append(taksonimi)
    sisseistumise_hind = float(rida[1])
    kilomeetri_hind = float(rida[2])
    
    hind = sisseistumise_hind + tee_pikkus*kilomeetri_hind
    taksode_hinnad.append(hind)
    
    indeks = 0
    miinimum = taksode_hinnad[0]
    for i in range(len(taksode_hinnad)):
        if taksode_hinnad[i] < miinimum:
            miinimum = taksode_hinnad[i]
            indeks = i
            
print("Kõige odavam on " + nimed[indeks] + ".")

f.close()