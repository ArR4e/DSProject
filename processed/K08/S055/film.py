def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="UTF-8")
    sisu = f.readlines()
    f.close()
    return [rida.strip().split(" - ")[0] for rida in sisu if rida.strip().split(" - ")[1] == žanr]
    
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write(f"\n{nimi} - {žanr}")
    f.close()
    
def kustutaFilm(nimi):
    f1 = open("filmid.txt", "r", encoding="UTF-8")
    sisu = f1.readlines()
    f1.close()
    
    f2 = open("filmid.txt", "w", encoding="UTF-8")
    a = [rida for rida in sisu if rida.strip().split(" - ")[0] != nimi]
    f2.writelines(a)
    f2.close()
    