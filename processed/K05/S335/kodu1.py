nimi = input("Sisestage oma kasutajanimi: ")
parool1 = input("Sisestage oma parool: ")
parool2 = input("Sisestage oma parool uuesti: ")

def numbri_olemasolu(a):
    for number in a:
        if number.isdigit():
            return False

while parool1 != parool2 or len(parool1) < 8 or numbri_olemasolu(parool1) == None or parool1.isnumeric():
    print("Parool on vigane.")
    parool1 = input("Sisestage oma parool: ")
    parool2 = input("Sisestage oma parool uuesti: ")

parool1 = parool1[::-1]
f = open("users.txt", "w")
f.write(nimi + ":" + str(parool1))
f.close()
