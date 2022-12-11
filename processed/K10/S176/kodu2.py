def võitja(mäng):
    võtmed = {}
    for i in range(4):
        for j in range(2):
            if mäng[i][j] == mäng[i][j+1] == mäng[i][j+2] == "X":
                võtmed["X"] = võtmed.get("X", 0) + 1
                võtmed["O"] = võtmed.get("O", 0) + 0
            elif mäng[i][j] == mäng[i][j+1] == mäng[i][j+2] == "O":
                võtmed["O"] = võtmed.get("O", 0) + 1
                võtmed["X"] = võtmed.get("X", 0) + 0
            else:
                võtmed["X"] = võtmed.get("X", 0) + 0
                võtmed["O"] = võtmed.get("O", 0) + 0
    for j in range(4):
        for i in range(2):
            if mäng[i][j] == mäng[i+1][j] == mäng[i+2][j] == "X":
                võtmed["X"] = võtmed.get("X", 0) + 1
                võtmed["O"] = võtmed.get("O", 0) + 0
            elif mäng[i][j] == mäng[i+1][j] == mäng[i+2][j] == "O":
                võtmed["O"] = võtmed.get("O", 0) + 1
                võtmed["X"] = võtmed.get("X", 0) + 0

    for i in range(2):
        for j in range(2):
            if mäng[i][j] == mäng[i+1][j+1] == mäng[i+2][j+2] == "X":
                võtmed["X"] = võtmed.get("X", 0) + 1
                võtmed["O"] = võtmed.get("O", 0) + 0
            elif mäng[i][j] == mäng[i+1][j+1] == mäng[i+2][j+2] == "O":
                võtmed["O"] = võtmed.get("O", 0) + 1
                võtmed["X"] = võtmed.get("X", 0) + 0
                
    for i in range(2):
        for j in range(2, 4):
            if mäng[i][j] == mäng[i+1][j-1] == mäng[i+2][j-2] == "X":
                võtmed["X"] = võtmed.get("X", 0) + 1
                võtmed["O"] = võtmed.get("O", 0) + 0
            elif mäng[i][j] == mäng[i+1][j-1] == mäng[i+2][j-2] == "O":
                võtmed["O"] = võtmed.get("O", 0) + 1
                võtmed["X"] = võtmed.get("X", 0) + 0

    return võtmed
