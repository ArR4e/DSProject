fail = open("taksohinnad.txt", "r", encoding="utf-8")
km = float(input("Sisesta tee pikkus kilomeetrites: "))
hinnad = []
hinnadkokku={}
for rida in fail:
    hinnad.append(rida.strip("\n").split(","))
if len(hinnad)==0:
    print("fail on tühi")
else:        
    for rida in hinnad:
        hind = float(rida[1])+float(rida[2])*km
        hinnadkokku.update({hind:rida[0]})
    print(hinnadkokku[min(hinnadkokku)])
