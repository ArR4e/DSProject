import film

def töötleKäsk(order, string):
    if order == 'K':
        while True:
            list = film.loetleFilmid(string)
            if list != []: 
                print("Filmid on: ")
                for el in list:
                    print(el)
                return True
                break
            else:
                string = input("Sisesta muu žanr: ")
    elif order == 'L':
        name = string.split()[1]
        genre = string.split()[0]
        film.lisaFilm(name, genre)
        print("Lisatud!")
        return True
    elif order == 'V':
        film.kustutaFilm(string)
        print("Head vaatamist!")
        return True
    elif order == 'E':
        return False
    
sisend = input("Sisesta käsklused: ")
list = sisend.split()
order = list[0]
del list[0]
string = ' '.join(list)
töötleKäsk(order, string)


