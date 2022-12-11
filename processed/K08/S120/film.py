
def load_file():
    names = []
    genres = []
    with open('filmid.txt', encoding='utf8') as f:
        data = f.readlines()
        for line in data:
            split_line = line.strip().split(' - ')
            names.append(split_line[0])
            genres.append(split_line[1])
    
    return names, genres


def loetleFilmid(input_genre:str):
    names, genres = load_file()
    
    output_list = []
    for i, genre in enumerate(genres):
        if genre.lower() == input_genre.lower():
            output_list.append(names[i])
    
    return output_list


def lisaFilm(input_name:str, input_genre:str):
    names, genres = load_file()
    
    names.append(input_name)
    genres.append(input_genre)
    with open('filmid.txt', 'w', encoding='utf8') as f:
        for i, name in enumerate(names):
            f.write(' - '.join([name, genres[i]])+'\n')
    

def kustutaFilm(input_name:str):
    names, genres = load_file()
    
    index = names.index(input_name)
    names.pop(index)
    genres.pop(index)
    with open('filmid.txt', 'w', encoding='utf8') as f:
        for i, name in enumerate(names):
            f.write(' - '.join([name, genres[i]])+'\n')
