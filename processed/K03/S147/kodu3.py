arv = int(input("Palun sisestage üks naturaalarv: "))
astendatav_arv = arv
liidetav_arv = arv
ruutude_summa = 0
summa = 0
for i in range(arv):
    ruutude_summa += astendatav_arv**2
    astendatav_arv -= 1
for i in range(arv):
    summa += liidetav_arv
    liidetav_arv -= 1
summa_ruut = summa**2
print("ühest", str(arv)+"ni täisarvude summa ruudu ja ühest", str(arv)+"ni ruutude summa erinevus on", summa_ruut-ruutude_summa)