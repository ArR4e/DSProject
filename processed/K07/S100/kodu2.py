f = open("taksohinnad.txt", "r")
arr = f.readlines()

teepikkus = float(input("Sisesta tee pikkus km: "))

uusarr = []

for i in arr:
    temp = i.split(",")
    uusarr.append([float(temp[1]) + float(temp[2])*teepikkus, temp[0]])
try:
    uusarr = sorted(uusarr,  key=lambda x: x[0])
    print(f"Kõige odavam on {uusarr[0][1]}.")
except:
    print("")