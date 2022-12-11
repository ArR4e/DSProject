fail = open("users.txt", "w")
def tagurpidi(nimi):
    return nimi[::-1]
kasutajanimi = input("Sisestage kasutajanimi: ")
parool = input("Sisestage parool: ")
parool2 = input("Sisestage parool: ")
if parool != parool2 or len(parool) < 8 or parool.isalpha() or parool.isnumeric():
    print("error")
else:
    teistpidi = tagurpidi(parool)
    fail.write(kasutajanimi + ":" + teistpidi)
    fail.close()