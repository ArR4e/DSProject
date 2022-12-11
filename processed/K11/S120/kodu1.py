
def seosta_lapsed_ja_vanemad(kids_file, names_file):
    kid_and_parents = {}
    
    with open(kids_file, encoding='utf8') as f:
        parent_kid = []
        for line in f:
            parent_kid.append(line.strip().split())
    
    with open(names_file, encoding='utf8') as f:
        names = {}
        for line in f:
            split_line = line.strip().split()
            name = ' '.join(split_line[1:])
            code = split_line[0]
            names[code] = name

    for pair in parent_kid:
        kid_and_parents[names[pair[1]]] = set()
    
    for pair in parent_kid:
        kid_and_parents[names[pair[1]]].add(names[pair[0]])
    

    return kid_and_parents


seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')