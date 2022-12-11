väljak = [['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]

def võitja(maatriks):    
    võidud = {"O": 0,
             "X": 0}
    for i, rida in enumerate(maatriks):
        for j, el in enumerate(rida):
            if el == "X" or el == "O":
                #horisontaalne kontroll (kontrollib esimest kaht elementi)
                if j < 2:
                    kolmjär = rida[j:j+3]
                    if kolmjär.count(el) == 3:
                        võidud[el] += 1
                if i < 2:
                    #vertikaalne kontroll
                    if el == maatriks[i+1][j] == maatriks[i+2][j]:
                        võidud[el] += 1
                    if j < 2:
                        if el == maatriks[i+1][j+1] == maatriks[i+2][j+2]:
                            võidud[el] += 1
                            
                    else:
                        if el == maatriks[i+1][j-1] == maatriks[i+2][j-2]:
                            võidud[el] += 1
                        
                
    print(võidud)                    
    return võidud