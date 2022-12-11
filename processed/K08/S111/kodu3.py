import film as filmidenimekiri

def töötleKäsk(käsk, järjend):
    if käsk=="K":
        print ("Võimalikud filmid on: \n" + str(filmidenimekiri.loetleFilmid(järjend)))
        return True
    elif käsk=="L":
        filmidenimekiri.lisaFilm(järjend[1], järjend[0])
        print ("Film on lisatud sinu listi!")
        return True
    elif käsk=="V":
        filmidenimekiri.kustutaFilm(järjend)
        print("Film on sinu riiulist kustutatud. \nHead vaatamist!")
        return True
    elif käsk=="E":
        return False
                
print("=== FILMIANDMEBAAS === \n",
      "Kuva filmid: K <žanr> \n",
      "Lisa film:   L <žanr> <film> \n",
      "Vaata filmi: V <filmi nimi> \n",
      "Lõpeta:      E \n",
      "=======================")
sisend=input()
sisend=sisend.split(" ")
käsk=sisend[0]
if len(sisend)==2:
    järjend=sisend[1]
    töötleKäsk(käsk, järjend)
elif len(sisend)==3:
    järjend=(sisend[1], sisend[2])
    töötleKäsk(käsk, järjend)
elif käsk=="E":
    järjend=[]
    töötleKäsk(käsk, järjend)
