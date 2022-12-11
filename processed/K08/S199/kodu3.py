from film import loetleFilmid(zanr)

def töötleKäsk(käsk, järjend):
    if käsk == "K":
        loetleFilmid(järjend)
        print:("Võimalikud filmid on: ")
        for i in filmid:
            print(i)
töötleKäsk("K", "märul")