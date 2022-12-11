f = open('taksohinnad.txt', 'r', encoding = 'UTF-8')
tee_pikkus_km = float(input('Sisesta tee pikkus kilomeetrites: '))
nimed = []
hinnad = []

for rida in f:
    andmed = rida.strip().split(",")
    takso_nimi = andmed[0]
    takso_sisseastumis_hind = float(andmed[1])
    km_hind = float(andmed[2])
    takso_hind = takso_sisseastumis_hind + km_hind * tee_pikkus_km
    nimed.append(takso_nimi)
    hinnad.append(takso_hind)
    väikseim_hind = min(hinnad)
    i = hinnad.index(väikseim_hind)
    soodsaim = nimed[i]
    
print('Kõige odavam on ' + soodsaim + '.')