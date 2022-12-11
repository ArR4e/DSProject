f = open("taksohinnad.txt", "r", encoding="UTF-8")
taxi = []
km_hind = []
skolko = float(input("Sisesta tee pikkus kilomeetrites: "))
for i in f:
    taksod = i.split(',')[0]
    sitdown = float(i.split(',')[1])
    hind = float(i.split(',')[2])
    result = sitdown + hind*skolko
    taxi.append(taksod)
    km_hind.append(result)
try:
    minimal = min(km_hind)
    indeks = km_hind.index(minimal)
    print("Kõige odavam takso on", taxi[indeks])
except:
    print("poshel nahui")
f.close()
    



    

