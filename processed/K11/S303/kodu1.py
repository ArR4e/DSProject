def seosta_lapsed_ja_vanemad(file_1, file_2):
    return_dict = {}
    name_dict = {}
    id_list = [[],[]]
    with open(file_1) as f_1, open(file_2) as f_2:
        for line in f_2:
            name_dict[line.split()[0]] = f'{line.split()[1]} {line.split()[2]}'
            
        for line in f_1:
            id_list[0].append(line.split()[0])
            id_list[1].append(line.split()[1])
            
        for i in range(len(id_list[0])):
            if name_dict[id_list[1][i]] not in return_dict.keys():
                return_dict[name_dict[id_list[1][i]]] = {name_dict[id_list[0][i]]}
            else:
                return_dict[name_dict[id_list[1][i]]].add(name_dict[id_list[0][i]])

    return return_dict
        
child_parent_dict = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for name in child_parent_dict:
    print(f'{name}: {", ".join(child_parent_dict[name])}')
