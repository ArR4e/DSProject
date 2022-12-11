nimi = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parooli: ")
    parool2 = input("Sisesta parooli veel kord: ")
    if parool1 == parool2 and len(parool1) >= 8:
        tagurpidi = parool1[::-1]
        break
    else:
        print("Vale. Parool peab sisaldama vähemalt 8 tähemarki (tähed ja numbrid).")
f = open("users.txt", "w")
f.write(nimi)
f.write(":")
f.write(tagurpidi)
f.close()


        