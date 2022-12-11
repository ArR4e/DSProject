fail = open("kinganumbrid.txt")

line_count = 0
for line in fail:
    if line != "\n":
        line_count += 1

fail.close()

teisendatud = 0

fail = open("kinganumbrid.txt")

while teisendatud < line_count:
    try:
        suurus = (float(fail.readline().strip()))
        pikkus = ((2/3)*((suurus)-2))
        teisendatud += 1
        print((round((pikkus))))
    except:
        teisendatud += 1
        print("Vigane sisend")

fail.close()



