def võitja(([[' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' ']])):
    
    # kas tegu on X või O ja mitu korda seda esineb
    x_loendur = 0
    if sümbol == "X":
        x_loendur += 1
        
    o_loendur = 0
    if sümbol == "O":
        o_loendur += 1
        
    # mitu korda järjest sümbolit esineb
