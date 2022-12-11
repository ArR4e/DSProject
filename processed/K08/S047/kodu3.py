from film import*

def töötleKäsk(käsk, järjend):
  
    if käsk == "K":
        print(loetleFilmid(järjend[0]))
    if käsk == "L":   
        film = " ".join(järjend[1:])
        lisaFilm(film, järjend[0])
    elif käsk == "V":
        kustutaFilm(järjend[0:])
    elif käsk == "E":
        return False

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <Kustuta film>\nLõpeta:      E\n===")

while True:
    sisend=input("Sisesta käsk: ")
    jupid=sisend.split(" ")
    käsk = jupid[0]
    if käsk == "E":
        break
    
    järjend = jupid[1:]
    töötleKäsk(käsk, järjend)
    
    
