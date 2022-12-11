import film

def töötleKäsk(a,b):
    if a == 'K':
        for el in b:
            zanr = el
        filmid = film.loetleFilmid(zanr)
        if len(filmid) == 0:
            print('Sellise žanriga filmi pole')
            return True
        else:
            print('Võimalikud flimid on:')
            for a in filmid:
                print(a)
            return True
    elif a == 'L':
        if len(b) > 0:
            zanr = b[0]
            b.remove(zanr)
            movie = ''
            for el in b:
                movie += el + ' '
            movie = movie.strip(' ')
            film.lisaFilm(movie, zanr)
            print('Film lisatud!')
        else:
            print('Filmi ei lisatud')
        return True
    elif a == 'V':
        c = ''
        for el in b:
            c += el + ' '
        c = c.strip(' ')
        if film.kustutaFilm(c) == True:
            print('Film nimekirjast kustutatud!')
            print('Head vaatamist!')
        else:
            print('Filmi ei vaadatud')
        return True
    else:
        return False

print('=== FILMIANDMEBAAS ===')
print('Kuva filmid: K <žanr> ')
print('Lisa film:     L <žanr> <film> ')
print('Vaata filmi:  V <filmi nimi> ')
print('Lõpeta:       E ')
print('===')

v = True
while v == True:
    i = input('>  ')
    i = list(i.split(' '))
    a = i[0]
    i.remove(a)
    v = töötleKäsk(a,i)
    
    

#print()
# filmid = film.loetleFilmid(K)
# print('>  K  ' + K)
# print('Võimalikud flimid on:')
# for a in filmid:
#     print(a)
# 
# print()
# print()

# print('>  L  ' + L)
# 
# lisa = L.split(' ')
# if len(lisa) > 0:
#     film.lisaFilm(lisa[1], lisa[0])
#     print('Film lisatud!')
# else:
#     print('Filmi ei lisatud')
# print()
# print()

# print('> ' + V)
# if film.kustutaFilm(V) == True:
#     print('Film nimekirjast kustutatud!')
#     print('Head vaatamist!')
# else:
#     print('Filmi ei vaadatud')

    




    