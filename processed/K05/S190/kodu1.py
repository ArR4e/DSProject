def on_numbrid_ja_tahed(parool):
    täht = False
    number = False
    for sümbol in parool:
        if str.isdigit(sümbol):
            number = True
        if str.isalpha(sümbol):
            täht = True
    return täht and number

kasutajanimi = input("Sisesta oma kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
    if parool1 != parool2:
        print("Paroolid ei ühti.")
        continue
    if len(parool1) < 8:
        print("Parool on liiga lühike.")
        continue
    if not on_numbrid_ja_tahed(parool1):
        print("Ei ole kasutatud numbreid ja tähti")
        continue
    else:
        tagurpidi = parool1 [::-1]
        fail = open("users.txt","w")
        fail.write(kasutajanimi+":"+tagurpidi)
        print("Info failis.")
        break

fail.close()
        
        

    