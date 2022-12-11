f = open("taksohinnad.txt", encoding="utf-8")

teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
taksode_kulu = []
taksode_info = []
i = 0

for rida in f:
    taksode_info += [rida.strip().split(',')]
    taksode_kulu += [float(taksode_info[i][1]) + float(taksode_info[i][2])*teepikkus]
    i += 1

if taksode_info != []:
    odavaim = taksode_info[taksode_kulu.index(min(taksode_kulu))][0]
    print(f"Kõige odavam on {odavaim}.")
else:
    print("Hinnakiri on tühi.")

f.close()