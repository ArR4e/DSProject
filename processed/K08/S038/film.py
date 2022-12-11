f = open("filmid.txt","r",encoding = "utf-8")
lines = f.readlines()
f.close()



def loetleFilmid(nimi):
    fail = open("filmid.txt","r+",encoding = "utf-8")
    filmid = []
    loetelu = ""
    while True:
        for line in fail:
            fail2 = line.split(" - ")
            if "" in fail2:
                break
            if str(nimi)+"\n" in fail2:
                loetelu = str(fail2[0])
                filmid += loetelu.split(" ")
        return(filmid)
        fail.close()
        
def lisaFilm(filmiNimi,zanr):
    lisa = open("filmid.txt","a",encoding = "utf-8")
    lisa.write("\n" +str(filmiNimi)+" - "+str(zanr)+"\n")
    lisa.close()
    

def kustutaFilm(nimetus):
    with open("filmid.txt","w",encoding = "utf-8") as new:
        for line in lines:
            nline = line.strip("\n")
            nwline = nline.strip(" ")
            if nwline.split(" - ")[0] != str(nimetus):
                new.write(line)

print(loetleFilmid("multikas"))
    
        
        
    
    