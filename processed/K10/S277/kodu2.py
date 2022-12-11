game = [['O','X','X',' '],
        [' ',' ','O','X'],
        [' ','O',' ','X'],
        ['O',' ',' ','X']]

def hori(game):
    pooled = ['X', 'O']
    winsdict = {}
    uuswindict = {}
    uuswindict = winsdict
    
    for pool in pooled:
        winsdict[pool] = 0
        
    for row in game:
        for pool in pooled:
            if pool*4 in ''.join(row):
                 uuswindict[pool] = winsdict[pool] + 2
            elif pool*3 in ''.join(row):
                uuswindict[pool] = winsdict[pool] + 1
            else:
                continue
    return uuswindict

def diag(game):
    pooled = ['X', 'O']
    winsdict = {}
    uuswindict = {}
    uuswindict = winsdict
    
    for pool in pooled:
        winsdict[pool] = 0
    for pool in pooled:
        if pool*4 in ''.join([game[i][i] for i in range(len(game))]):
            uuswindict[pool] = winsdict[pool] + 2
        elif pool*3 in ''.join([game[i][i] for i in range(len(game))]): #Suur diagonaal vasakult paremale
            uuswindict[pool] = winsdict[pool] + 1
        if pool*4 in ''.join([game[i][len(game) - i - 1] for i in range(len(game))]):
            uuswindict[pool] = winsdict[pool] + 2
        elif pool*3 in ''.join([game[i][len(game) - i - 1] for i in range(len(game))]): # Suur diagonaal paremalt vasakule
            uuswindict[pool] = winsdict[pool] + 1
    return uuswindict

def vert(game):
    import numpy
    return hori(numpy.transpose(game))
    
            
print(hori(game), diag(game), vert(game))


