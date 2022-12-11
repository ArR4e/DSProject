#plokkskeem
#list on hea algoritmilise andmetöötluse jaoks

n = input("Mis on sinu kasutajanimi?")

p1 = input("Mis on kasutajanime parool?")

p2 = input("Korda parooli")


while True:
    if p1 == p2:
        break
    if p1 != p2:
        print("Esimene ja teine parool ei ühti")
    p1 = input("Mis on kasutajanime parool?")
    p2 = input("Korda parooli")
while True:
    if len(p1) >= 8:
        break
    if len(p1) < 8:
        print("Parool on liiga lühike")
    p1 = input("Mis on kasutajanime parool?")
    p2 = input("Korda parooli")
list = []
#tühi list, mida täitma hakatakse selle suhtes rakendava appendiga
while True:
    for i in p1:
        y = i.isnumeric()
        s = str(y)
        list.append(s)
#selleks, et listida, tuleb luua see muutuja kujule, mida hiljem asendada protsesside käigus
    x = len(p1)
    y = list.count("False")
    z = list.count("True")

    if x != y:
        break
    if x == y:
        print("Sisesta parool tähemärkide ja numbritega")
    p1 = input("Mis on kasutajanime parool?")
    p2 = input("Korda parooli")
#parooli tagurpidi pööramine
list2 = []
for i in p1:
    y1 = i
    s1 = str(y1)
    list2.append(s1)


r = list2.reverse()
#reverse pöörab nimekirja tagasi
string= ""
#tühi muutuja, mida join vajab - et anda liidetud listile string väärtuse, peab join kaasama listi stringi. Parim on selleks tühi string.
#tühi string võib ka olla "".join(list2) kujul ehk siis otsesel kujul.
#string.join(iterable)
j = string.join(list2)
#print(j)

#kirjuta kasutajanimi ja parool faili users.txt kujul: loorap
f = open("users.txt", "w")
f.writelines(str(n))
#f.writelines("\n")
f.writelines(":")
f.writelines(str(j))
f.close()