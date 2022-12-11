#Kusib kasutajalt naturaalarvu
number=int(input("Sisesta siia naturaalarv:"))
#Arvutab ruutude summa ja umardab selle
ruutude_summa = round((number*(number+1)*(2*number+1))/6)
#Arvutab naturaalarvude summa ruudu ja umardab selle
summa_ruut = round((number*(number+1)/2)**2)
#Valjastab summa ruudu ja ruutude summa erinevuse
print("Summa ruudu ja ruutude summa erinevus on " + str(summa_ruut-ruutude_summa)+".")