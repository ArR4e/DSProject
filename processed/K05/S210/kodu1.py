import re
def onnumber(value):
    numbrid = re.findall('[0-9]', value)
    return False if numbrid else True

kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool esimest korda: ")
    parool2 = input("Sisesta parool teist korda: ")
    if parool2 != parool1:
        print("Paroolid ei kattu!")
    elif len(parool1) <8:
        print ("Parool on liiga lühike!")
    elif onnumber(parool1):
        print("Parool peab sisaldama numbrit!")
    else:
        break
reverse = parool1 [::-1]

f= open("users.txt", "w")
f.write(kasutajanimi + ":" +reverse)
f.close()