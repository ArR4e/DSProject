km = float(input("Mitu kilomeetrit koju?: "))
f = open("taksohinnad.txt")
read_arv = f.readlines()
best = ""
parim = 0
for i in read_arv:
    rida = i.strip().split(",")
    maksumus = (km * float(rida[2]) + float(rida[1]))
    if parim == 0:
        parim = maksumus
        best = rida[0]
    elif maksumus < parim:
        parim = maksumus
        best = rida[0]
f.close()

print("parim teenus on " + best)
    
    