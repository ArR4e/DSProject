from film import *

def töötleKäsk(seis, sisu):
    if seis == "K":
        print(loetleFilmid(str(sisu[0])))
        return True
    elif seis == "L":
#         nimi = str(sisu[1:])
        print(sisu)
        lisaFilm(sisu[1], sisu[0])
        print("Film lisatud!")
        return True
    elif seis == "V":
        print(sisu[0])
        kustutaFilm(str(sisu[0]))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif seis == "E":
        exit()
    else:
        print("Tundmatu käsk, proovi uuesti!")
        return True
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid:  K <žanr>")
print("Lisa film:    L <žanr> <film>")
print("Vaata filmi:  V <filmi nimi>")
print("Lõpeta:       E ")
print("===")

while True:
    inp = input("> ")
    uus = inp.split(" ")
    käsk = uus[0]
    k = 0
    lol = []
    lol = uus[1:]
    if käsk == "V":
        lol = []
        lol.append(inp[2:])
    if käsk == "L":
        lol = []
        uus2 = []
        uus2 = inp[2:]
        appi = "".join(uus2).split(" ")
        idk = appi[1:]
        aaa = " ".join(idk)
        lol.append(appi[0])
        lol.append(aaa)
#         lol.append(uus[1])
#         lol.append(uus[2:])
#         while k < len(lol[1]):
#             uus2 = uus2 + lol[1][k]
#             k += 1
#         lol[1] = uus2
#         while k < len(uus[1:]):
#             lol = 
        print(aaa)
#     if käsk == "V" or käsk == "K":
#         lol.append(uus)
#     elif käsk == "L":
#         lol.append(uus[2:])
#     while k < len(uus) -1:
#         lol.append(uus[k+1])
#         k += 1
    töötleKäsk(käsk, lol)