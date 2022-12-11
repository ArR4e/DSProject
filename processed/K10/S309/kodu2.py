from collections import Counter

def võitja(m):

    dictionary = {}
    dictionary.update({"O":0})
    dictionary.update({"X":0})

    #read
    for i in range(0,4):
        
        if m[i].count("X") == 4:
            dictionary["X"] += 2
        elif m[i].count("X") == 3:
            if (m[i][1] and m[i][2]) == "X":
                    dictionary["X"] += 1
        if m[i].count("O") == 4:
            dictionary["O"] += 2
        elif m[i].count("O") == 3: 
            if (m[i][1] and m[i][2]) == "O":
                    dictionary["O"] += 1

    #veerud
    for i in range(0,4):
        line = [m[0][i], m[1][i], m[2][i], m[3][i]]

        if line.count("X") == 4:
            dictionary["X"] += 2
        elif line.count("X") == 3:
            if (line[1] and line[2]) == "X":
                    dictionary["X"] += 1
        if line.count("O") == 4:
            dictionary["O"] += 2
        elif line.count("O") == 3:
            if (line[1] and line[2]) == "O":
                    dictionary["O"] += 1

    #diagonaalid
    #alumised paremale shiftida
    line1 = m[0] + [' ',' ',' ']
    line2 = [' '] + m[1] + [' ',' ']
    line3 = [' ',' '] + m[2] + [' ']
    line4 = [' ',' ',' '] + m[3]
    rightlist = [line1, line2, line3, line4]

    #alumised vasakule shiftida
    line1 = [' ',' ',' '] + m[0]
    line2 = [' ',' '] + m[1] + [' ']
    line3 = [' '] + m[2] + [' ',' ']
    line4 = m[3] + [' ',' ',' ']

    leftlist = [line1, line2, line3, line4]

    for i in range(0,7):
        line = [rightlist[0][i], rightlist[1][i], rightlist[2][i], rightlist[3][i]]
        if line.count("X") == 4:
            dictionary["X"] += 2
        elif line.count("X") == 3:
            if (line[1] and line[2]) == "X":
                    dictionary["X"] += 1
        if line.count("O") == 4:
            dictionary["O"] += 2
        elif line.count("O") == 3:
            if (line[1] and line[2]) == "O":
                    dictionary["O"] += 1

    for i in range(0,7):
        line = [leftlist[0][i], leftlist[1][i], leftlist[2][i], leftlist[3][i]]
        if line.count("X") == 4:
            dictionary["X"] += 2
        elif line.count("X") == 3:
            if (line[1] and line[2]) == "X":
                    dictionary["X"] += 1
        
        if line.count("O") == 4:
            dictionary["O"] += 2
        elif line.count("O") == 3:
            if (line[1] and line[2]) == "O":
                    dictionary["O"] += 1

    return dictionary

print(võitja([  ['O',' ','O','X'],
                ['O','O','X','X'],
                ['O','X','O',' '],
                ['X','X','X','O']]))

