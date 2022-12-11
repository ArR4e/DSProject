def lististamine(n):
    x = list(n.split(","))
    return x

f = open("taksohinnad.txt", "r")
failisisu = f.readlines()

uus_list = []

for rida in failisisu:
    rida.rstrip()
    y = lististamine(rida)
    
    for element in y:
        uus_list.append(element.strip())
        

list_arvudega = []

m = 0
for element in uus_list:
    try:
        list_arvudega.append(float(element))
    except:
        list_arvudega.append(element)


#koguhind = alghind + kmhind * teepikkus

teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
väikseim_hind = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

i = 0
while i < len(uus_list):
    taksonimi = uus_list[i]
    koguhind = list_arvudega[i+1] + (teepikkus * list_arvudega[i+2])
    if float(koguhind) < väikseim_hind:
        väikseim_hind = koguhind
    i = i + 3


i = 0
while i < len(uus_list):
    taksonimi = uus_list[i]
    koguhind = list_arvudega[i+1] + (teepikkus * list_arvudega[i+2])
    if väikseim_hind == koguhind:
        print("Kõige odavam on " + taksonimi)
        break
    else:
        i = i + 3
        continue