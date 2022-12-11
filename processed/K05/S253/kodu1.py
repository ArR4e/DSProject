
nimi = input("Sisestage kasutajanimi: ")
pass1 = ""
pass2 = ""
while True:

    pass1 = input("Sisestage parool: ")
    pass2 = input("Sisestage parool uuesti: ")

    if not pass1 == pass2:
        print("Sisestatud paroolid ei klapi.")
        continue
    
    if not len(pass1) >= 8:
        print("Teie parooli pikkus peab olema vähemalt 8.")
        continue

    if pass1.isalpha() or pass1.isnumeric():
        print("Teie parool peab sisaldama nii tähti kui ka numbreid.")
        continue

    break

temp_jarjend = []
tagurpidi_parool = ""

for letter in pass1:
    temp_jarjend.insert(0, letter) 

for letter in temp_jarjend:
    tagurpidi_parool += letter

f = open("users.txt", "a+")
f.write(nimi + ":" + tagurpidi_parool + "\n")

f.close()




