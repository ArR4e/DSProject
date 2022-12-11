a = input("Sisesta kasutajanimi: ")
b = input("Sisesta parool esimest korda: ")
c = input("Sisesta parool teist korda: ")

for parool in b:
    if b == c and len(b) >= 8:
        b[::-1]
    else:
        break

file = open("users.txt", "w")
file.write(a + ":" + b[::-1])
file.close()