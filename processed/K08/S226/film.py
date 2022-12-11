#функция открывает файл filmid.txt и возвращает список фильмов по жанру. 
def loetleFilmid(žanri_nimetus): # Очередность фильмов не важна, но список должен содержать все название фильмов соответствующих жанру.
    fail = open("filmid.txt", encoding="UTF-8")
    for rida in fail:
        fail.readline().strip
        rida = rida.split(" - ")
    
    




def lisaFilm(filmi_nimi, žanri_nimetus): # функция открывает файл и записывает туда новый ряд в нужном виде.
    fail = open('filmid.txt', "a", encoding="utf-8")
    fail.write("\n")
    fail.write(filmi_nimi + " - ")
    fail.write(žanri_nimetus)
    fail.close() #tootab
    
    
def kustutaFilm(filmi_nimi): # функция открывает файл и убирает от ряд , где записан фильм.
    fail = open('filmid.txt', "r")
    lines = fail.readlines()
    fail.close()
    with open("filmid.txt", "w") as fail:
        for line in lines:
            if line.strip('\n') != filmi_nimi:
                fail.write(line)


# 
# loetleFilmid("multikas")

file = open("filmid.txt", encoding="UTF-8")
for rida in file:
    file.readline().strip
    
    rida = rida.split(" - ")
    print(rida)
  