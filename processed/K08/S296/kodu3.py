import film
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <zanr>"+"\n"+"Lisa film: L <zanr> <filmi nimi>"+"\n"+"Vaata filmi: V <filmi nimi>"+"\n"+"Lõpeta: E"+"\n"+"===")
#sisend = input("")
#sisend = sisend.split(" ")
#T = sisend[0]
#järjend = sisend[1]
#järjend_2 = sisend[2]


def töötleKäsk(T, järjend):
    if T == 'K':
        print("Võimalikud filmid on:")
        for i in film.loetleFilmid(järjend):
            print(i)
        return True
    if T == 'L':
        järjend_2 = järjend.split(" ")
        järjend_3 = ""
        for i in järjend_2:
            if i == järjend_2[0]:
                continue
            elif i != järjend_2[-1]:
                järjend_3 = järjend_3+ i +" "
            else:
                järjend_3 = järjend_3 + i
        film.lisaFilm(järjend_3,järjend_2[0])
        print("Film lisatud!")
        return True
    if T == 'V':
        film.kustutaFilm(järjend)
        print("Fail nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    if T == 'E':
        return False 

väärtus= True
while väärtus != False:
    sisend = input("")
    sisend = sisend.split(" ")
    järjend= ""
    T = sisend[0]
    if len(sisend) != 1:
        for i in sisend:
            if i == sisend[0]:
                continue
            elif i != sisend[-1]:
                järjend = järjend+ i +" "
            else:
                järjend = järjend + i
    else:
        järjend = " "
    väärtus=töötleKäsk(T,järjend)




