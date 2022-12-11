nimi = str(input("Sisestage kasutajanimi: "))

numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    parool = str(input("Sisestage parool: "))
    parool2 = str(input("Sisestage parool uuesti: "))
    if parool != parool2:
        print("Esimene parool peab kattuma teise parooliga.")
        continue
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemärki.")
        continue
    elif not any(c in numbers for c in parool):
        print("Parool peab sisaldama numbreid.")
        continue
    elif not any(c in letters for c in parool):
        print("Parool peab sisaldama tähti.")
        continue
    parool = "".join(reversed(parool))
    break

f = open("users.txt", "w")
f.write(nimi+":"+parool)
f.close()
print(parool)