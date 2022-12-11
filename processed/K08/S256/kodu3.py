import film
v = 0
while v < 1:
    sisend = input("Sisesta Command: ")
    if sisend.startswith("K"):
        sisend = sisend.split(" ")
        valikud_list = film.loetleFilmid(sisend[1])
        sisend = ""
        for i in valikud_list:
            sisend += i + ", "
        sisend = sisend[0:len(sisend)-2]
        print("Sinu filmivalikud on: "+ sisend)
    
    elif sisend.startswith("L"):
        sisend = sisend.split(" ")
        Lisatavfilm = " ".join(sisend[1:len(sisend)-1])
        film.lisaFilm(Lisatavfilm, sisend[-1])
        print(Lisatavfilm + " on lisatud nimekirja")
    elif sisend.startswith("V"):
        sisend = sisend.split(" ")
        Kustutatavfilm = " ".join(sisend[1:len(sisend)])
        film.kustutaFilm(Kustutatavfilm)
        print(Kustutatavfilm + " on kustutatud")
    elif sisend.startswith("E"):
        print("programm on lõpetatud")
        v += 1
    else:
        print("midagi oli sisendis viga")