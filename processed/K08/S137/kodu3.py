import film
def töötlekäsk(käsk, param):
    if käsk != 'E':
        if käsk == 'K':
            filmid = film.loetleFilmid(param[0])
            if len(filmid) == 0:
                print("sellise zanriga filmi pole")
                return
            print("Võimalikud filmid on:")
            for el in filmid:
                print (el)
            return True
        elif käsk == 'L':
            film.lisaFilm(param[1],param[0])
            print("Film lisatud!")
            return True
        elif käsk == 'V':
            film.kustutaFilm(param[0])
            print("Film nimekirjast kustutatud!"+'\n'+'Head vaatamist!')
            return True
        if käsk == 'E':
            return False
        
            
    
    

while True:
    a = input("Sisesta käsk:")
    a= a.split(' ')
    a2 =[]
    a3 = ['']
    a1 = a[0]
    if a1 != 'E':
        a2 += [a[1]]
        if a1 == 'L':
            a2 += [a[2]]
        elif a1 == 'V':
            for el in a:
                if a[0] == el or a[1]==el:
                    continue
                a2[0]+=' '+el
            print(a2)
    print(a2)
    if töötlekäsk(a1,a2) == False:
        break
