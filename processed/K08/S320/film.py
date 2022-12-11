def loetleFilmid(žanr):
    f=open("filmid.txt", encoding="UTF-8")
    filmid=[]
    for i in f.readlines():
        jupid=i.split(" - ")
        if žanr==jupid[1].strip():
            filmid.append(jupid[0].strip())
        
    f.close()   
    return filmid
            
def lisaFilm(filmi_nimi,žanr):
    f=open("filmid.txt", "a",encoding="UTF-8")
    f.write("\n "+ filmi_nimi + " - "+ žanr)
    f.close()

def kustutaFilm(filmi_nimi):
    f=open("filmid.txt", encoding="UTF-8")
    lines=f.readlines()
    f.close()
    
    newfile=open("filmid.txt", "w", encoding="UTF-8")
    
    for rida in lines:
        jupid=rida.split(" - ")
        if filmi_nimi!=jupid[0].strip():
            newfile.write(rida)
    newfile.close() 