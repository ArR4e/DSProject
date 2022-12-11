pikkus = float(input("Sisesta tee pikkus kilomeetrites :"))

odavaim_takso_hind = "määramata"
odavaim_takso = 0

def odavaim_hind(nimi, istumine, km_hind):
    print(type(km_hind))
    print(type(pikkus))
    print(type(istumine))
    hind = float(km_hind) * pikkus + float(istumine)
    if odavaim_takso_hind == "määramata":
        odavaim_takso_hind = float(hind)
        odeavaim_takso = nimi
    elif hind < odavaim_takso_hind:
        odavaim_takso_hind = hind
        odeavaim_takso = nimi

f = open("taksohinnad.txt")
tekst = f.readlines()

tekst = [el.strip() for el in tekst]

taksod = ()

taksod = [el.split(",") for el in tekst]

for takso in taksod:
    print(takso)
    
    for el in takso:
        print(el)
        nimi = el[0]
        istumine = el[1]
        km_hind = el[2]
        odavaim_hind(nimi, istumine, km_hind)
        
print(odavaim_takso_hind)
print(odavaim_takso)
