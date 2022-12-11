nimi = input("Sisestage kasutajanimi: ")
parol1 = input("Sisestage parool: ")
parol2 = input("Sisestage parool veel kord: ")
while parol1 != parol2:
    print("Teises paroolis on midagi puudu, proovige uuesti!")
    parol1 = input("Sisestage parool: ")
    parol2 = input("Sisestage parool veel kord: ")
while len(parol1 and parol2) < 8:
    print("Parool on liiga lühike, proovige pikendada!")
    parol1 = input("Sisestage parool: ")
    parol2 = input("Sisestage parool veel kord: ")
while parol1.isnumeric() or parol1.isalpha():
    print("Teie paroolis peavad olema tähemärgid koos numbritega!")
    parol1 = input("Sisestage parool: ")
    parol2 = input("Sisestage parool veel kord: ")
    
def reverse(a):
    a = parol2[::-1]
    return a

faili_nimi = "users.txt"
f = open("users.txt", "w")
f.write(nimi + ":" + str((reverse(parol2))))
f.close()
    

    