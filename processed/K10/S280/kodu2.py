# 2. Trips-traps-trull / RP

def võitja(maatriks):
    seisX = 0
    seisY = 0
    seisXY = 0
    võitX = 0
    seisYX = 0
    võitY = 0
    skoor = {}
    for r,rida in enumerate(maatriks):
        for i, el in enumerate(rida):
            if el == "X":
                seisX += 1
                seisY += 1
                seisXY += 1
                seisYX += 1
                try:
                    if rida[i+1] == "X" and rida[i+2] == "X":
                        seisX += 2
                except:
                    pass
                try:
                    if maatriks[r+1][i] == "X" and maatriks[r+2][i] == "X":
                        seisY += 2
                except:
                    pass
                try:        
                    if maatriks[r+1][i+1] == "X" and maatriks[r+2][i+2] == "X":
                        seisXY += 2
                except:
                    pass
                try:
                    if r-2 >= 0:
                        if maatriks[r-1][i+1] == "X" and maatriks[r-2][i+2] == "X":
                            seisYX += 2
                except:
                    pass
                if seisX == 3:
                    võitX += 1
                if seisY == 3:
                    võitX += 1
                if seisXY == 3:
                    võitX += 1
                if seisYX == 3:
                    võitX += 1
                seisX = 0
                seisY = 0
                seisXY = 0
                seisYX = 0
                
            elif el == "O":
                seisX += 1
                seisY += 1
                seisXY += 1
                seisYX += 1
                try:
                    if rida[i+1] == "O" and rida[i+2] == "O":
                        seisX += 2
                except:
                    pass
                try:
                    if maatriks[r+1][i] == "O" and maatriks[r+2][i] == "O":
                        seisY += 2
                except:
                    pass
                try:        
                    if maatriks[r+1][i+1] == "O" and maatriks[r+2][i+2] == "O":
                        seisXY += 2
                except:
                    pass
                try:
                    if r-2 >= 0:
                        if maatriks[r-1][i+1] == "O" and maatriks[r-2][i+2] == "O":
                            seisYX += 2
                except:
                    pass
                if seisX == 3:
                    võitY += 1
                if seisY == 3:
                    võitY += 1
                if seisXY == 3:
                    võitY += 1
                if seisYX == 3:
                    võitY += 1
                seisX = 0
                seisY = 0
                seisXY = 0
                seisYX = 0
    skoor["O"] = võitY
    skoor["X"] = võitX
    return skoor
    
print(võitja([[' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' ']]))
