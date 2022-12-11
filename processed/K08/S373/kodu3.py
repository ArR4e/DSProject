from film import *

def töötleKäsk(tähis, argumendid):
    if tähis == "K":
        i = 0
        esimenev = loetleFilmid(argumendid)
        if esimenev == []:
            return False
        print("\n", "Võimalikud filmid on: ")
        while i < len(esimenev):
            print(esimenev[i])
            i += 1
        return True
    elif tähis == "L":
        lisaFilm(list2[1], list2[0])
        return True
    elif tähis == "V":
        kustutaFilm(argumendid)
        return True
    elif tähis == "E":
        return False

list1 = []
list2 = []
list3 = []
x = 2
y = 1

while True:
    sisestus = input("")
    if sisestus[0] == "K":
        väärtus1 = sisestus.split()
        while töötleKäsk(väärtus1[0], väärtus1[1]) == False:
            print("\n", "Tekstifailis pole soovitud žanrist ühtegi filmi.", "\n", "Valige mõni muu žanr.")
            väärtus1 = input("\n", "Kuva filmid: ").split()
        continue
    elif sisestus[0] == "L":
        väärtus2 = sisestus.split()
        while x < len(väärtus2):
            list1.append(väärtus2[x])
            x += 1
        list2.append(väärtus2[1])
        list2.append(" ".join(list1))
        print("\n", "Film lisatud!")
        print()
        print(töötleKäsk(väärtus2[0], list2))
        list1 = []
        list2 = []
        x = 2
        continue
    elif sisestus[0] == "V":
        väärtus3 = sisestus.split()
        while y < len(väärtus3):
            list3.append(väärtus3[y])
            y += 1
        print("\n", "Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        print()
        print(töötleKäsk(väärtus3[0], " ".join(list3)))
        list3 = []
        y = 1
        continue
    elif sisestus[0] == "E":
        break