kasutajanimi=input("Kasutajanimi: ")

while True:
    uusparool=input("Loo uus parool: ")
    parool=input("Korda parooli: ")
    if parool!=uusparool:
        print("Paroolid ei kattu")
    if len(uusparool)<8:
        print("Parool liiga lühike")
    if uusparool.isalpha() or uusparool.isdigit():
        print("Parool peab sisaldama numbreid ja tähti")
    else:
        break
    
uusparool=uusparool[len(uusparool):0:-1]+uusparool[0]

f=open("users.txt","a")
f.write(kasutajanimi+":"+uusparool+"\n")
f.close()

print("Kasutaja salvestatud")