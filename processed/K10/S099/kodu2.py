def võitja(mäng):
    vastus = {'O': 0, 'X' : 0}
    #vasakult-paremale
    for i in range(4):
        for j in range(2):
            if mäng[i][j] != ' ' and mäng[i][j] == mäng[i][j+1] == mäng[i][j+2]:
                vastus[mäng[i][j]] += 1
    #ülevalt alla
    for i in range(2):
        for j in range(4):
            if mäng[i][j] != ' ' and mäng[i][j] == mäng[i+1][j] == mäng[i+2][j]:
                vastus[mäng[i][j]] += 1
    #diagonaal paremale-alla
    for i in range(2):
        for j in range(2):
            if mäng[i][j] != ' ' and mäng[i][j] == mäng[i+1][j+1] == mäng[i+2][j+2]:
                vastus[mäng[i][j]] += 1
    #diagonaal paremale-üles
    for i in range(2,4):
        for j in range(2):
            if mäng[i][j] != ' ' and mäng[i][j] == mäng[i-1][j+1] == mäng[i-2][j+2]:
                vastus[mäng[i][j]] += 1         
    return vastus
    

print(võitja([['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]))