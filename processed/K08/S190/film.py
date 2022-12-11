
def loetleFilmid(zanri_nimi):
    fail_filmid = open("filmid.txt")
    ühe_zanri_filmid = []
    for rida in fail_filmid:
        
        rea_element = rida.split(" - ")
        zanr = rea_element[-1].rstrip()
        filmi_nimi = rea_element[-2]
        if zanr == zanri_nimi:
            ühe_zanri_filmid.append(filmi_nimi)
    
    fail_filmid.close()
        
    return ühe_zanri_filmid
            

def lisaFilm(nimi,zanr):
    fail_filmid = open("filmid.txt","a")
    fail_filmid.write("\n"+nimi+" - "+zanr)
    fail_filmid.close()
        
        
def kustutaFilm(Filmi_Nimi):
    fail_filmid = open("filmid.txt")
    uus_nimekiri = []
    for rida in fail_filmid:
        rea_element = rida.split(" - ")
        film_nimi = rea_element[0].rstrip()
        if film_nimi != Filmi_Nimi:
            uus_nimekiri.append(rida)
    fail_filmid.close()
    
    fail_filmid = open("filmid.txt","w")
    for element in uus_nimekiri:
        fail_filmid.write(element)
    fail_filmid.close()
        
