nimi = input("Sisestage kasutajanimi: ")
while True:
    pass1 = input("Sisestage parool: ")
    pass2 = input("Sisestage parool uuesti: ")
    
    if pass1 == pass2 and len(pass1) >= 8 and not pass1.isalpha() and not pass1.isnumeric():
        break
    else:
        print("Kontrollige kas teie paroolis on numbrid, tähed, on vähemalt 8 tähemärki pikk ning kas mõlemad paroolid on samad.")

passr = ""
for i in pass1:
    passr = i + passr
f = open("users.txt", "a")
f.write(nimi+":"+passr+"\n")
f.close()