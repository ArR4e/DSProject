import film
def töötleKäsk(käsk, järjend):
    if käsk=="E":
        tagastus=False
    if käsk=="L":
        film.lisaFilm(järjend[1], järjend[0])
        print("Film lisatud!")
        tagastus=True
    if käsk=="K":
        filmid=film.loetleFilmid(järjend[0])
        if filmid==[]:
            print("Sellest žanrist filme ei ole!")
        else:
            print("Võimalikud filmid on: " + str(filmid))
        tagastus=True
    if käsk=="V":
        film.kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!" + "\nHead vaatamist!")
        tagastus=True
    return(tagastus)
print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===")
while True:
    a=str(input()).split()
    b=[]
    c=a[0]
    if len(a)==4:
        b.append(a[1])
        b.append(a[2]+ " " + a[3])
    if len(a)==3:
        b.append(a[1])
        b.append(a[2])
    if len(a)==2:
        b.append(a[1])
    if töötleKäsk(c, b)==False:
        break

      
        
        
        
