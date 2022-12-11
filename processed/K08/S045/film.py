global FILENAME
FILENAME = 'filmid.txt'

def read_file():
    with open(FILENAME, 'r', encoding='UTF-8') as f:
        data = f.readlines()
    zanrid = {}
    
    for item in data:
        items = item.split(' - ')
        if items[1].strip() not in zanrid:
            zanrid[(items[1].strip())] = []
        zanrid[items[1].strip()].append(items[0].strip())
        
    return zanrid

def loetleFilmid(zanr):
    filmid = read_file()
    if zanr.strip() in filmid:
        return filmid[zanr.strip()]
    else:
        return []

def lisaFilm(film, zanr):
    with open(FILENAME, 'r', encoding='UTF-8') as f:
        data = f.readlines()
    if len(data) != 0:
        if not data[len(data) - 1].endswith('\n'):
            data.append('\n')
    data.append(f'{film} - {zanr}\n')
    with open(FILENAME, 'w', encoding='UTF-8') as f:
        f.writelines(data)
        
def kustutaFilm(film):
    with open(FILENAME, 'r', encoding='UTF-8') as f:
        data = f.readlines()
    new_data = []
    for line in data:
        if not (line.strip()).startswith(film):
            new_data.append(line)
    
    with open(FILENAME, 'w', encoding='UTF-8') as f:
        f.writelines(new_data)
