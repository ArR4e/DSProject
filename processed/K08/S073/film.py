def load():
    with open("filmid.txt", encoding="UTF-8") as f:
        a = list()
        for row in f.readlines():
            a.append(row.strip().split(" - "))
        return a

def loetleFilmid(genre):
    movies = load()
    mov = list()
    for movie in movies:
        if movie[1] == genre: mov.append(movie[0])
    return mov

def lisaFilm(name, genre):
    curr = load()
    currStr = list()
    for i in curr:
        currStr.append(" - ".join(i)+"\n")

    currStr.append(f"{name} - {genre}\n")

    print(currStr)
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        f.writelines(currStr)

def kustutaFilm(name):
    curr = load()
    currStr = list()
    for i in curr:
        if not i[0] == name:
            currStr.append(" - ".join(i) + "\n")

    print(currStr)
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        f.writelines(currStr)