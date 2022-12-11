kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool = str(input("Sisesta soovitud parool: "))
    parool2 = str(input("Sisesta parool uuesti: "))
    if parool != parool2:
        print("Sisestatud esimene parool ei kattu teisega.")
    elif len(parool) < 8:
        print("Parool on liiga lühike.")
    elif parool.isalpha():
        print("Parool ei sisalda numbreid.")
    elif parool.isnumeric():
        print("Parool ei sisalda tähti.")
    else:
        break
        
tagurpidi = parool[::-1]

fail = open("users.txt", "w")
fail.write(str(kasutajanimi) + ":" + str(tagurpidi))
fail.close()

