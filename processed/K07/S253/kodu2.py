
ans = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", "r+", encoding="UTF-8" )

hinnad = []
nimed = []

for rida in f:
    split_rida = rida.strip().split(',')
    nimed.append(split_rida[0])
    hind = float(split_rida[1]) + float(ans*float(split_rida[2]))
    hinnad.append(hind)
if ans > 0:
    vaikseim_hind_index = hinnad.index(min(hinnad))
    vaikseim_hind = nimed[vaikseim_hind_index]

    print("Kõige odavam on " + vaikseim_hind + ".")
else:
    print()