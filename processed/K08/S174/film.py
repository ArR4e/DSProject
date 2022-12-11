def loetleFilmid(žanr):
    fail = open("filmid.txt")
    filmid = fail.readlines() #tekib list kõikidest faili ridadest
    tulemusjärjend = [] #seda tahan väljastada, filmide list
    for rida in filmid:
        if žanr in rida:
            filmilist = rida.split(" - ") #rida.split(" - ") teeb ühe rea listiks kahe erineva elemendiga - märgi juurest
            filminimi = filmilist[0] #0ndal kohal on filmi nimi
            tulemusjärjend.insert(0, filminimi)
    fail.close()
    return tulemusjärjend
            
    
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a") #"a" lisab teksti tekstifaili, "w" kirjutaks üle
    rida = "\n" + nimi + " - " + žanr #reavahetus
    fail.write(rida)
    fail.close()

def kustutaFilm(nimi):
    fail = open("filmid.txt", "r")
    read = fail.readlines()
    fail.close()
    fail = open("filmid.txt", "w")
    for rida in read:
        #selleks, et sarnaseid nimesid eristada, teeme rea listiks
        #ja võtame selle listi 0ndal kohal oleva elemendi(filminimi)
        if nimi != rida.split(" - ")[0]: 
            fail.write(rida)
    fail.close()
    #loeb faili, näeb, et nt Moanat ei ole, siis kirjutab kõik teised read uuesti v.a Moana
    
#kustutaFilm("Moana")
    


