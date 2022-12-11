from film import *

#  ​K <žanr>
#  ​L <žanr> <filmi nimi>
#  ​V <filmi nimi>
#  ​E

def töötleKäsk(tahis, arg_jarjend):
    
    if tahis == "K":
        filmid = loetleFilmid(arg_jarjend[0])
        print("Võimalikud filmid on: ")
        for film in filmid:
            print(film)
        return True
            
    elif tahis == "L":
        lisaFilm(arg_jarjend[1], arg_jarjend[0])
        print("Film lisatud!")
        return True
        
    elif tahis == "V":
        kustutaFilm(arg_jarjend[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
        
    elif tahis == "E":
        return False
  
  
print('''
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
''')

while True:
    sisend = input("")
    kask = sisend[0]
    arg_jarjend = []
    
    if kask == "K":
        arg = sisend[2:]
        arg_jarjend.append(arg)
        
    elif kask == "L":
        argid = sisend[2:]
        argi_jupid = argid.split()
        
        zanr = argi_jupid[0]
        arg_jarjend.append(zanr)  # Leian žanri ja nime ja lisan need listi
        
        i = len(zanr) - 1
        filmi_nimi = argid[i+2:]
        arg_jarjend.append(filmi_nimi)
        
    elif kask == "V":
        arg = sisend[2:]
        arg_jarjend.append(arg)
    
        
    x = töötleKäsk(kask, arg_jarjend)
    if x == False:
        break