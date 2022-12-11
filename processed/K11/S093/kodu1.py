def seosta_lapsed_ja_vanemad(file1, file2):
    nimed_dict = {}
    seosed = {}
    
    nimed = open(file2, 'r')
    nimed_lines = nimed.readlines()
    nimed.close()
    
    for line in nimed_lines:
        line = line.replace('\n', '').split(' ')
        
        nimed_dict[line[0]] = line[1] + ' ' + line[2]
        
    lapsed = open(file1, 'r')
    lapsed_lines = lapsed.readlines()
    lapsed.close()
    
    for lapsed in lapsed_lines:
        lapsed = lapsed.replace('\n', '').split(' ')
        lapse_nimi = nimed_dict[lapsed[1]]
        
        if lapse_nimi not in seosed:
            seosed[lapse_nimi] = set()
        seosed[lapse_nimi].add(nimed_dict[lapsed[0]])
        
    for lapsed in seosed:
        print(lapsed + ': ', end = '')
        print(*seosed[lapsed], sep=', ')
    return seosed
seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
    