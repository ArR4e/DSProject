from pykkar import *
laius = int(input('Sisesta maailma laius: '))
pikkus = int(input('Sisesta maailma pikkus: '))
loc_x = int(input("Sisesta mis ruudus alustab robotimees x-teljel: "))
loc_y = int(input("Sisesta mis ruudus alustab robotimees y-teljel: "))

trellide_rida = laius * "#" + "\n" 
vahepealne = "#" + ((laius - 2) * " " + "#") + "\n"

maailm = trellide_rida
for i in range(1, pikkus - 1):
    temp = vahepealne
    if i == loc_y:
        list_a = list(vahepealne)
        list_a[loc_x] = ">"
        temp = "".join(list_a)
    maailm += temp

maailm += trellide_rida

create_world(maailm)

nurgad = 4
while not is_wall():
        step()
while nurgad > 0:
    right()
    while not is_wall():
        step()
    paint()
    nurgad -= 1