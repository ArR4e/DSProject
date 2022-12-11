def loetleFilmid(žanr):
    fail = open('filmid.txt', encoding = "UTF-8")
    filmi_nimed = []
    for rida in fail:
        rida = rida.strip()
        rea_osad = rida.split(" - ")
        filmi_nimi = rea_osad[0]
        filmi_žanr = rea_osad[1]
        if filmi_žanr == žanr:
            filmi_nimed += [filmi_nimi]
    fail.close()
    return filmi_nimed

def lisaFilm(nimi, žanr):
    fail = open('filmid.txt', "a", encoding = "UTF-8")
    fail.write('\n' + nimi + " - " + žanr)
    fail.close()
    

def kustutaFilm(film):
    fail = open('filmid.txt', "r", encoding = "UTF-8")
    rea_number = -1
    for rida in fail:
        rida = rida.strip()
        rea_osad = rida.split(" - ")
        rea_number += 1
        if film in rea_osad:
            kustutatav_rida = rea_number
    fail.close()

    fail2 = open('filmid.txt', "r", encoding = "UTF-8")
    read = fail2.readlines()
    fail2.close()
    
    uus_fail = open('filmid.txt', "w+", encoding = "UTF-8")
    
    del read[kustutatav_rida]
    
    for rida in read:
        uus_fail.write(rida)

    uus_fail.close()



    
