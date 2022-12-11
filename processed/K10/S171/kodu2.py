def parem(a, x, y, c, mitu):
    if mitu == 3:
        return 1
    elif x + 1 > 3:
        return 0
    elif a[y][x + 1] != c:
        return 0
    else:
        mitu += 1
        return parem(a, x + 1, y, c, mitu)


def down(a, x, y, c, mitu):
    if mitu == 3:
        return 1
    elif y + 1 > 3:
        return 0
    elif a[y + 1][x] != c:
        return 0
    else:
        mitu += 1
        return down(a, x, y + 1, c, mitu)


def pall(a, x, y, c, mitu):
    if mitu == 3:
        return 1
    elif y + 1 > 3 or x + 1 > 3:
        return 0
    elif a[y + 1][x + 1] != c:
        return 0
    else:
        mitu += 1
        return pall(a, x + 1, y + 1, c, mitu)


def vall(a, x, y, c, mitu):
    if mitu == 3:
        return 1
    elif y + 1 > 3 or x - 1 < 0:
        return 0
    elif a[y + 1][x - 1] != c:
        return 0
    else:
        mitu += 1
        return vall(a, x - 1, y + 1, c, mitu)


def võitja(a):
    tulemus = {'O': 0, 'X': 0}
    for y in range(4):
        for x in range(4):
            if a[y][x] != ' ':
                mitu = 1
                tulemus[a[y][x]] += parem(a, x, y, a[y][x], mitu) + down(a, x, y, a[y][x], mitu) + \
                                    pall(a, x, y, a[y][x], mitu) + vall(a, x, y, a[y][x], mitu)
    return tulemus

print(võitja([[' ', 'X', ' ', 'O'],
              [' ', 'X', ' ', 'O'],
              [' ', 'X', ' ', 'O'],
              [' ', ' ', ' ', ' ']]))
        
