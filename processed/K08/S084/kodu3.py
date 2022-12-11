from film import *
def töötleKäsk(cmd,arg):
    if cmd == "K":
        filmid = loetleFilmid(arg)
        print("Võimalikud filmid on:")
        for x in filmid:
            print(x)
        tagastus = True
    elif cmd == "L":
        txt = arg.split()
        del txt[0]
        lisaFilm(" ".join(txt),arg.split()[0])
        print("Film lisatud!")
        tagastus = True
    elif cmd == "V":
        kustutaFilm(arg)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        tagastus = True
    elif cmd == "E":
        tagastus = False
    return tagastus
print("== FILMIANDMEBAAS ==")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")
while True:
    try:
        sisestus = input()
        if not töötleKäsk(sisestus[0],sisestus[2:len(sisestus)]):
            break
    except:
        print("Midagi läks valesti")