maatriks1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
maatriks2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
maatriks3 = [[4, 31, 67, 99]]

def transponeeriK(maatriks):
    tr_järjend = []
    uus_järjend = []
    for i in range (-1, -(len(maatriks[0]))-1, -1):
        uus_järjend = []
        for järjend in maatriks:
            viimaneel = järjend[i]
            uus_järjend.append(viimaneel)
        uus_järjend.reverse()
        tr_järjend += [uus_järjend]
    print(tr_järjend)
    return tr_järjend