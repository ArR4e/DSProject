import film
def töötleKäsk(tähis, järjend):   
    if tähis == 'K':
       print("Võimalikud filmid on: " + '\n')
       print(film.loetleFilmid(järjend)) 
       return(True)
    if tähis == 'L':
       W = []
       w = järjend.split(" ")
       žanr = w[0]
       nimi = w[1]
       tegevus = film.lisaFilm(nimi, žanr)
       return(True)
    if tähis == 'V':
      film.kustutaFilm(järjend)
      return(True)
    if tähis == 'E':
      return(False)

a = input("Kuva filmid: ")
x = a.split(" ")
käsk_a = x[0]
žanr_a = x[1]

b = input("Lisa film: ")
y = b.split(" ",1)
käsk_b = y[0]
järjend_b = y[1]
töötleKäsk(käsk_b,järjend_b)

c = input("Vaata filmi: ")
z = c.split(" ")
käsk_c = z[0]
nimi_c = z[1]
töötleKäsk(z[0],z[1])

d = input("Lõpeta: ")

print(a)
print(töötleKäsk(käsk_a,žanr_a))
print(b)

print("Film lisatud!")
print(c + '\n' + "Film kustutatud, head vaatamist!")
print(d)
