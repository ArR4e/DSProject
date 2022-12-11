km = float(input("Sisesta tee pikkus km-tes: "))
f = open("taksohinnad.txt", encoding = "UTF-8")

n = []
h = []
kh = []

k = 1

for rida in f:
    for sona in rida.split(","):
        if k ==1:
            n.append(sona)
        elif k == 2:
            h.append(float(sona))
        else:
            kh.append(float(sona))
        k+=1
        if k == 4:
            k = 1
        
f.close()

odavaim = []

if len(n) > 0:
    for i in range(len(n)):
        summa = km * kh[i] + h[i]
        odavaim.append(summa)
    vastus = n[odavaim.index(min(odavaim))]
    print("Kõige odavam on " + vastus + ".")
    
else:
    print("Järjend on tühi!")
