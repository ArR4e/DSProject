def loetleFilmid(žanr):
    filmid = open("filmid.txt","r",encoding="utf-8")
    žanriga_filmid = []
    for rida in filmid:
        stripped = rida.strip().split(" - ")
        if stripped[1] == žanr:
            žanriga_filmid.append(stripped[0])
    filmid.close()
    if žanriga_filmid == []:
        print("Ühtegi sellise žanriga filmi ei leitud.")
    return žanriga_filmid

def lisaFilm(nimi,žanr):
    filmid = open("filmid.txt","a+",encoding="utf-8")
    filmid.write("\n"+nimi+" - "+žanr)
    filmid.close()
    
def kustutaFilm(nimi):
    filmid = open("filmid.txt","r",encoding="utf-8")
    tekst = filmid.readlines()
    filmid.close()
    for rida in range(len(tekst)):
        if tekst[rida].strip().split(" - ")[0] == nimi:
            print(f"kustutatud film {nimi}")
            tekst.pop(rida)
            break
    filmid = open("filmid.txt","w",encoding="utf-8")
    filmid.write("".join(tekst)) #ei saa aru, miks ta viimasest filmist osa veel lõppu liidab.
    filmid.close()