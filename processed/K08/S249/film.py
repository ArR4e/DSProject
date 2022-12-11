f = open("filmid.txt", encoding = "utf-8")


filmid = []
zanrid = []
    
for film in f:
    reaosad = film.split(" - ")
        
    film = reaosad[0]
    zanr = reaosad[1].strip()
    
    filmid = filmid + [film]
    zanrid = zanrid + [zanr]
        
def loetleFilmid(žanr):
    while True:            
        koikfilmid = []
        
        mitmes = zanrid.index
        
        film = zanrid.index(žanr)
        film = zanrid.index(žanr)
        koikfilmid += filmid[film].split(",")
        
        if film == "":
            break
    
        return koikfilmid

print(loetleFilmid("märul"))
f.close()
