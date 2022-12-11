liin = int(input("liini pikkus: "))
pmax = int(input("postide maksimaalne kaugus üksteisest: "))
tekst = str("minimaalne postide arv, mida on liini ehitamiseks vaja:")
j66k = liin % pmax
if j66k == 0:
    x = int(liin / pmax + 1)
    print(tekst + (str(x)))
else:
    while j66k > 0:
        pmax = pmax - 1
        j66k = liin % pmax
x = int(liin / pmax + 1)
print(tekst + (str(x)))