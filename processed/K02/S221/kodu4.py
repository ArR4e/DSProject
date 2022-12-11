#Puuduvad oskused et teha keerulisemat programmi
#Ei oska arvesse võtta mitte ettemääratuid ridu
f = open('inglise.txt')
rida1 = f.readline()
rida2 = f.readline()
rida3 = f.readline()
f.close()

rida1 = rida1.replace('Hello', 'Tere')
rida2 = rida2.replace('Hello', 'Tere')
rida3 = rida3.replace('Hello', 'Tere')

lugemiseks = rida1 + rida2 + rida3
asendus = lugemiseks.count('Tere')
print('Tehtud on ', asendus, ' asendust.')
f = open("eesti.txt", "w")

f.write(rida1)
f.write(rida2)
f.write(rida3)

f.close()