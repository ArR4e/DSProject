def võitja(laud):

    märgid = ["O","X"]
    punktid = {}

    for märk in märgid:
        punktid[märk] = 0
        for rida in laud:
            if rida[0] == märk and rida[1] == märk and rida[2] == märk:
                punktid[märk] += 1
            if rida[1] == märk and rida[2] == märk and rida[3] == märk:
                punktid[märk] += 1

        for i in range(4):
            if laud[0][i] == märk and laud[1][i] == märk and laud[2][i] == märk:
                punktid[märk] += 1
            if laud[1][i] == märk and laud[2][i] == märk and laud[3][i] == märk:
                punktid[märk] += 1

        for i in range(2):
            if laud[0][i] == märk and laud[1][i+1] == märk and laud[2][i+2] == märk:
                punktid[märk] += 1
            if laud[1][i] == märk and laud[2][i+1] == märk and laud[3][i+2] == märk:
                punktid[märk] += 1

        for i in range(2):
            if laud[2][i] == märk and laud[1][i+1] == märk and laud[0][i+2] == märk:
                punktid[märk] += 1
            if laud[3][i] == märk and laud[2][i+1] == märk and laud[1][i+2] == märk:
                punktid[märk] += 1

    return punktid