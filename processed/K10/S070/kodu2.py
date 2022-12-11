def võitja(jada):
    i = 0
    vastus = { 'O' : 0,
                 'X' : 0}
    for jada2 in jada:
        for el in jada2:
            if el == 'O':
                vastus['O'] += 1
            if el == 'X':
                vastus['X'] += 1
    return vastus

            
        
        