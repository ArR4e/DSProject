import re
nimi = input("Sisestage kasutajanimi: ")
parool1 = input("Sisestage parool: ")
parool2 = input ("Sisestage parool teist korda: ")

while parool1 != parool2:
    print("Kasutaja puudub.")
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool teist korda: ")

while len(parool1) < 8:
    print("Kasutaja puudub, parool on liiga lühike.")
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool teist korda: ")
    
while not (re.search('[0-9]',parool1)):
    print("Kasutaja puudub, paroolis peavad olema numbrid ka.")
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool teist korda: ")

parool = parool1[::-1]
fail = open("users.txt", 'w')
fail.write("kasutajanimi:")
fail.write(parool)
fail.close()