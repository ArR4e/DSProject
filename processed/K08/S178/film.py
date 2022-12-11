def loetleFilmid(sisend):
    f = open("filmid.txt", encoding = "UTF-8")
    nimed = []
    zanrid = []
    for rida in f:
        rea_osad = rida.split(" -") 
        nimi = rea_osad[0]
        zanr = rea_osad[1]
        zanr2 = [zanr.strip("\n")]
        if sisend in zanr:
            nimed = nimed + [nimi]
            #zanrid = zanrid + [zanr.strip("\n")]
    return(nimed)

    f.close()

#sisend = str(input("Sisesta filmizanr: "))
#print(loetleFilmid(sisend))


def lisaFilm(filmi_nimi,filmi_zanr):
    f = open("filmid.txt", mode="a", encoding = "UTF-8")
    sisu = ' - '.join([filmi_nimi, filmi_zanr])
    f.write("\n" + sisu)
    f.close
    

#filmi_nimi = str(input("Sisesta filminimi: "))
#filmi_zanr = str(input("Sisesta filmižanr: "))
#(lisaFilm(filmi_nimi,filmi_zanr))



def kustutaFilm(sisu):
    fail = open("filmid.txt", encoding = "UTF-8")
    tulemus = []
    for rida in fail:
        rea_osad = rida.split(" -") 
        nimi = rea_osad[0]
        if sisu in nimi:
            continue
        else:
            tulemus = tulemus + [rida]
    fail.close()
    kirjutamine = open("filmid.txt", "w", encoding = "UTF-8")
    sisu = ''.join(tulemus)
    kirjutamine.write(sisu)
    return(tulemus)
    kirjutamine.close()
    

#sisu = str(input("Sisesta kustutatava filmi nimi: "))
#(kustutaFilm(sisu))
    