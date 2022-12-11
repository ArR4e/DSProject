def loetleFilmid(sisestatud_žanr):
    fail = open("filmid.txt","r", encoding = "UTF-8")
    nimed = []
    
    for rida in fail:
        järjend = rida.split(" - ")
        
        nimi = järjend[0]
        
        žanr = järjend[1].strip()
        
        if žanr == sisestatud_žanr:
            nimed.append(nimi)
    
    fail.close()
 
    return nimed    
  

def lisaFilm(lisatav_nimi,lisatav_žanr):
    fail = open("filmid.txt","a", encoding = "UTF-8")
    fail.write("\n" + lisatav_nimi + " - " + lisatav_žanr )
    fail.close()
    


def kustutaFilm(kustutatav):
    fail = open("filmid.txt","r", encoding = "UTF-8")
    
    järjend = []
    
    järjend = fail.read().split("\n")
    
    fail.close()
    
    fail2 = open("filmid.txt","w", encoding = "UTF-8")
    
    for i in järjend:
        
        if i == "":
            break
        
        else:
            filmid = i.split(" - ")
            
            uuritav_nimi = filmid[0]
            uuritav_žanr = filmid[1]
            
            if kustutatav != uuritav_nimi:
                fail2.write(uuritav_nimi + " - " + uuritav_žanr + "\n")
            
    fail2.close()

# loetleFilmid("märul")
# lisaFilm("Borat","komöödia")
# kustutaFilm("Spider-Man")

