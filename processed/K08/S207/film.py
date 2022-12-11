def loetleFilmid(žanr):
    nimi = []
    with open("filmid.txt", encoding = "UTF-8") as fail:
        for rida in fail:
            rida = rida.strip().split(" - ")
            if rida[1] == žanr:
                nimi += [rida[0]]
    return nimi

def lisaFilm(nimi, žanr):
    with open("filmid.txt", "a+", encoding = "UTF-8") as fail:
        fail.write(f"\n{nimi.strip()} - {žanr.strip()}")

def kustutaFilm(nimi):
    tekst = ""
    with open("filmid.txt", "r+", encoding = "UTF-8") as fail:
        for rida in fail:
            rida = rida.split()
            if " ".join(rida[0:-2]) != nimi:
                tekst += str(" ".join(rida)) + "\n"
        fail.seek(0)
        fail.truncate(0)
        fail.write(tekst)