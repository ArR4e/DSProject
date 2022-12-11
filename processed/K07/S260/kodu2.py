distance = float(input("Sisesta tee pikkus kilomeetrites: "))

nimed = []
istumise_hind = []
km_hind = []

f = open("taksohinnad.txt","r",encoding="UTF-8")
data = f.readlines()

if data == []:
    print("Ei funka, taksohinnad.txt on tühi")
    quit()

for i in range(len(data)):
    temp = data[i].split(",")
    nimed.append(temp[0].strip())
    istumise_hind.append(temp[1].strip())
    km_hind.append(temp[2].strip())
    
i = 0
hind_t = float(istumise_hind[i])+float(float(distance)*float(km_hind[i]))
odavaim = 0

for i in range(len(data)):
    hind = float(istumise_hind[i])+float(float(distance)*float(km_hind[i]))
    if hind < hind_t:
        odavaim = i
        hind_t = float(istumise_hind[i])+float(float(distance)*float(km_hind[i]))
    
print("Kõige odavam on",nimed[odavaim]+".")
f.close()