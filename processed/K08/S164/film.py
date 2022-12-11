def lae_andmed():
    f = open("filmid.txt", encoding = "utf-8")
    read = []
    for rida in f:
        read = read + [rida.strip("\n")]
    f.close()
    
    return read

def lisa_read(filmid, mode):
    f = open("filmid.txt", mode, encoding = "utf-8")
    for film in filmid:
        f.write("\n")
        f.write(film)
    f.close()
    

def loetleFilmid(žanr):
    filmid = lae_andmed()
    filmi_nimed = []
    for film in filmid:
        filmi_andmed = film.split(" - ")
        filmi_žanr = filmi_andmed[1]
        if filmi_žanr == žanr:    
            filmi_nimed = filmi_nimed + [filmi_andmed[0]]  
    
    return filmi_nimed

def lisaFilm(nimi, žanr):
    filmi_nimi = [nimi + " - " + žanr]
    lisa_read(filmi_nimi, "a")

def kustutaFilm(filmi_nimi):
    filmid = lae_andmed()
    filmi_nimed = []
    
    for film in filmid:
        filmi_andmed = film.split(" - ")
        filmi_kustutatav_nimi = filmi_andmed[0]
        if filmi_kustutatav_nimi != filmi_nimi:
            filmi_nimed = filmi_nimed + [film]
            
    lisa_read(filmi_nimed, "w")
    
    #return filmi_nimed
#print(lisaFilm("Shrek", "multikas"))
#print(kustutaFilm("Shrek"))