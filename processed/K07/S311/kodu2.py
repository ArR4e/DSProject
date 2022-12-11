madalaim = 100000
km = float(input("Sisesta teepikkus koju: "))
f = open("taksohinnad.txt")
for i in f:
    uus = i.split(",")
    hind = float(uus[1]) + km*float(uus[2])
    if hind < madalaim:
        madalaim = hind
        virma = uus[0]
print("Kõige odavam on {}.".format(virma))
f.close()    