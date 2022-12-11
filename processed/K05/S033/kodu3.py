def moos(a, b, c):
    suuri = 0
    while c / 5 >= 1 and a > 0:
        suuri += 1
        c -= 5
        a -= 1
    if b >= c:
        return c + suuri
    else:
        return -1

print(moos(1, 0, 5))