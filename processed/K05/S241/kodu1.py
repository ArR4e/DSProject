kasutajanimi = input(str("Vali endale kasutajanimi: "))
parool_1 = input("Vali endale parool: ")
parool_2 = input("Sisesta parool uuesti: ")
parool_1_pikkus = len(parool_1)

def number(n):
    return any(char.isdigit() for char in n)
def täht(m):
    return any(char.isalpha() for char in m)

if parool_1 != parool_2:
    print("Sisestatud paroolid ei kattu.")
if parool_1_pikkus < 8:
    print("Parool on lühem kui kaheksa sümbolit, vali parool, milles on vähemalt kaheksa sümbolit.")
parool_1_number = number(parool_1)
if parool_1_number == 0:
    print("Paroolis pole ühtegi numbrit, kasuta vähemalt ühte numbrit.")
parool_1_täht = täht(parool_1)
if parool_1_täht == 0:
    print("Paroolis pole ühtegi tähte, kasuta vähemalt ühte tähte.")

def ümberpöörd(x):
  return x[::-1]
parool_tagurpidi = ümberpöörd(parool_1)

f = open("users.txt", "w")
f.write("kasutajanimi: " + kasutajanimi + "\n")
f.write("parool: " + parool_tagurpidi + "\n")
f.close()