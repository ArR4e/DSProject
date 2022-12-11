f = open("aadressid.txt", encoding="utf-8")

print("Kasutajanimed on:")

mitu = 0
for rida in f:
    if "http://www.ut.ee/~" in rida.strip():
        mitu += 1
        print(mitu)   # ei osanud lause seest nime välja tuua
        



f.close()