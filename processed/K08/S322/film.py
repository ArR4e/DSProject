
def loetleFilmid(žanr):
    filmid = []
    with open("filmid.txt", "r", encoding="UTF-8") as fail:
        for rida in fail.read().split("\n"):
            üksrida = rida
            poolitaja = rida.rfind("-")
            if üksrida[poolitaja+2:] == žanr:
                filmid.append(üksrida[:poolitaja-1])
    return filmid

def lisaFilm(film, žanr):
    uusrida = f"\n{film} - {žanr}"
    with open("filmid.txt", "a", encoding="UTF-8") as fail:
        fail.write(uusrida)

def kustutaFilm(film):
    filmid = []
    with open("filmid.txt", "r", encoding="UTF-8") as fail:
        for rida in fail.read().split("\n"):
            üksrida = rida
            poolitaja = rida.rfind("-")
            if not üksrida[:poolitaja-1] == film:
                filmid.append((üksrida[:poolitaja-1], üksrida[poolitaja+2:]))
    with open("filmid.txt", "w", encoding="UTF-8") as fail:
        esimenerida = True
        for film in filmid:
            if not esimenerida:
                fail.write("\n")
            else:
                esimenerida = False
            fail.write(f"{film[0]} - {film[1]}")
