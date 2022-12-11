nimi=input("Sisesta kasutajanimi: ")
while True:
    parool1=input("Sisesta parool esimest korda: ")
    parool2=input("Sisesta parool teist korda: ")
    if parool1 != parool2:
        print("Paroolid ei kattu.")
        continue
    if len(parool1) < 8:
        print("Parool on liiga lühike.")
        continue
    if parool1.isalpha() or parool1.isnumeric() == "True":
        print("Parool peab sisaldama nii tähti kui ka numbreid.")
        continue
    def tagurpidi(parool1):
        str=""
        for i in parool1:
            str = i + str
        return str
    f=open("users.txt", "w")
    f.write(nimi+":")
    f.write(tagurpidi(parool1))
    f.close()
    break