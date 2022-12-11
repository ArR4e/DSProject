f = open("taksohinnad.txt")

teepikkus = float(input("Mitu km koduni? "))

taksonimed = []
maksumused = []

for rida in f:
    v22rtused_eraldi = (rida.strip()).split(",")
    taksonimed += [v22rtused_eraldi[0]]
    alustushind = float(v22rtused_eraldi[1])
    kmhind = float(v22rtused_eraldi[2])
    maksumus = alustushind + kmhind*teepikkus
    maksumused += [maksumus]
    
v2ikseima_hinna_indeks = maksumused.index(min(maksumused))
print(f"Kõige odavam on {taksonimed[v2ikseima_hinna_indeks]}.")

f.close()