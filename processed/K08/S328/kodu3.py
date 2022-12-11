import film

print("======= FILMIANDMEBAAS ======")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("=============================")

def töötleKäsk(käsk, järjend):
    if käsk == "K":
        result_1 = film.loetleFilmid(järjend[0])
        print("Võimalikud filmid on:")
        [print(i) for i in result_1]
        return True
    
    elif käsk == "L":
        result = film.lisaFilm(järjend[1:], järjend[0])
        print("Film lisatud!")
        return True
    
    elif käsk == "V":
        result = film.kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
        
    elif käsk == "E":
        return False
    else:
        return True
        
while True:
    valik = input("")
    x = valik.split()
    käsk_1 = x[0]
    järjend_1 = x[1:]
    if töötleKäsk(käsk_1, järjend_1) is True:
        continue
    else:
         break
    
    


    
    
    
    

    
    
    
    
    

