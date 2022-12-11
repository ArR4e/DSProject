from film import*

def töötleKäsk(a,b):
    if a == "E":
        return False
    if a == "K":
        if loetleFilmid(b[0]) == []:
            print("Sellise žanri filme andmebaasis ei ole!")
        else:
            print("Võimalikud filmid on:")
            for el in loetleFilmid(b[0]):
                print(el)
        return True
    if a == "L":
        lisaFilm(b[1],b[0])
        print("Film lisatud!")
        return True
    if a == "V":
        kustutaFilm(b[0])
        print("Film on nimekirjast eemaldatud, head vaatamist!")
        return True
jätk = True
sõna = ""
while jätk == True:
    a = input()
    b = []
    if a[0] == "K":
        b.append(a.split()[1])
    elif a[0] == "V":
        b.append(a[2:len(a)])
    elif a[0] == "L":
        for i in range(2, len(a)-1):
            if a[i] == " ":
                b.append(sõna)
                b.append(a[i+1:len(a)])
                break
            else:
                sõna += a[i]
        
    jätk = töötleKäsk(a[0],b)

