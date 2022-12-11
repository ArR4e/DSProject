from film import *

def töötleKäsk(command, argument):
    if command == "K": #Kuva filmid
        print('Võimalikud filmid on:')
        print('\n'.join(loetleFilmid(argument[0])))
        return True
    elif command == "L": #Lisa film
        lisaFilm(' '.join(argument[1:]), argument[0])
        print('Film lisatud!')
        return True
    elif command == "V": #Vaata filmi
        kustutaFilm(' '.join(argument[0:]))
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
        return True
    elif command == "E": #Lõpeta (exit)
        return False

while True:
    user_input = input('').split(' ')
    if töötleKäsk(user_input[0], user_input[1:]):
        continue
    break