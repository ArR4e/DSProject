def võitja(järjärjend):
    d={
        'O':0,
        'X':0,
    }
    for järjend in range(len(järjärjend)):
        for el in range(len(järjärjend[järjend])):
            if järjärjend[järjend][el] =='O':
                #loeb paremale
                if el < 2 and järjärjend[järjend][el+1]=='O' and järjärjend[järjend][el+2]=='O':
                    d['O'] = d.get('O', 0) + 1
                #loeb alla
                if järjend < 2 and järjärjend[järjend+1][el]=='O' and järjärjend[järjend+2][el]=='O':
                    d['O'] = d.get('O', 0) + 1
                #loeb paremale alla
                if el < 2 and järjend < 2 and järjärjend[järjend+1][el+1]=='O' and järjärjend[järjend+2][el+2]=='O':
                    d['O'] = d.get('O', 0) + 1
                #loeb vasakule alla
                if el > 1 and järjend < 2 and järjärjend[järjend+1][el-1]=='O' and järjärjend[järjend+2][el-2]=='O':
                    d['O'] = d.get('O', 0) + 1
            if järjärjend[järjend][el] =='X':
                if el < 2 and järjärjend[järjend][el+1]=='X' and järjärjend[järjend][el+2]=='X':
                    d['X'] = d.get('X', 0) + 1
                if järjend < 2 and järjärjend[järjend+1][el]=='X' and järjärjend[järjend+2][el]=='X':
                    d['X'] = d.get('X', 0) + 1
                if el < 2 and järjend < 2 and järjärjend[järjend+1][el+1]=='X' and järjärjend[järjend+2][el+2]=='X':
                    d['X'] = d.get('X', 0) + 1
                if el > 1 and järjend < 2 and järjärjend[järjend+1][el-1]=='X' and järjärjend[järjend+2][el-2]=='X':
                    d['X'] = d.get('X', 0) + 1
    return d

