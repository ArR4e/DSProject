kasutajanimi = input("Sisesta kasutajanimi: ")

def number_täht(sõna):
    kas_number = False
    kas_täht = False
    for i in sõna:
        if i.isalpha():
            kas_täht = True
        if i.isdigit():
            kas_number = True
    return kas_täht and kas_number

def tagurpidi(s):
    return s[::-1]

while True:
    parool = input("Sisesta parool: ")
    parool2 = input("Sisesta parool: ")
    if parool == parool2:
        pikkus = len(parool)
        if pikkus >= 8:
            if number_täht(parool) == True:
                tagurpidiparool = tagurpidi(parool)
                f = open("users.txt", "w")
                f.write(kasutajanimi + ":" + tagurpidiparool)
                f.close()
                print("Kasutajanimi ja parool on failis users.txt :)")
                break
            else:
                print("Parool sisaldagu vähemalt 1 tähte ja 1 numbrit!")
        else:
            print("Liiga lühike parool!")
    else:
        print("Paroolid ei klapi!")