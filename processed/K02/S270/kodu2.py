import math
x = input('Sisestage liini pikkus: ')
y = input('Sisestage postidevaheline max kaugus: ')
def liin(kaugus, maxpost):
    return math.ceil(int(kaugus)/int(maxpost)) + 1
print(liin(x, y))