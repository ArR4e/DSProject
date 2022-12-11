def parool():
    global parool1
    parool1 = input("Kirjuta parool: ")
    global parool2
    parool2 = input("Kirjuta parool uuesti: ")

kasutajanimi = input("Kirjuta kasutajanimi: ")
parool()

while True:
    if parool1 != parool2:
        print("Paroolid peavad omavahel kattuma!")
        parool()
    elif len(parool1) and len(parool2) < 8:
        print("Parooli pikkus peab olema vähemalt 8 tähemaärki!")
        parool()
    elif parool1.isalpha() or parool1.isnumeric():
        print("Parool peab sisaldam tähti ja numbreid!")
        parool()
    else:
        break

parool_tagurpidi = parool1[::-1]
#https://www.w3schools.com/python/python_howto_reverse_string.asp - sain siit abi

fail = open("users.txt", "w")
fail.write(kasutajanimi + ":" + parool_tagurpidi)
fail.close()