odavaim = 0
odavaim_nimi = 0
nimed = []
sisenemine = []
km =[]
t = (input("Sisesta tee pikkus km: "))
f = open("taksohinnad.txt")
for rida in f:
    rida = f.readline()
    rea_inf = [rida.split(",")]
    info = rea_inf[:]
    nimed.append(info[0])
    sisenemine.append(info[1])
    km.append(info[2])
    
for hind in km:
    hind = km[:]*t + sisenemine[:]
if 0 < hind < odavaim :
         odavaim = hind
         nimi = odavaim_nimi

print("Kõige odavam on ", odavaim_nimi)
