def loetleFilmid(genre):
    file = open("filmid.txt", encoding = 'utf-8')
    list = []
    for line in file:
        line = line.strip()
        line = line.split(' - ')
        if genre in line:
            list += [line[0]]
    file.close()
    return list

def lisaFilm(name, genre):
    with open("filmid.txt", 'a', encoding = 'utf-8') as file:
        file.write('\n' + name + ' - ' + genre)
    file.close()
    
def kustutaFilm(name):
    file = open("filmid.txt", encoding = 'utf-8')
    lines = file.readlines()
    for line in lines:
        if name in line:
            index = lines.index(line)
            del lines[index]
    text = ''.join(lines)
    file.close()
    with open("filmid.txt", 'w', encoding = 'utf-8') as file:
        file.write(text)
    file.close()
    


        