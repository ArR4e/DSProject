n = float(input("Sisesta naturaalarv: "))

n2 = float(n + 1)
n3 = float(n2 + 1)
n4 = float(n3 + 1)
n5 = float(n4 + 1)
n6 = float(n5 + 1)
n7 = float(n6 + 1)
n8 = float(n7 + 1)
n9 = float(n8 + 1)
n10 = float(n9 + 1)



summaruut = (n ** 2 + n2 ** 2 + n3 ** 2 + n4 ** 2 + n5 ** 2 + n6 ** 2 + n7 ** 2 + n8 ** 2 + n9 ** 2 + n10 ** 2)
ruutudesumma = (n + n2 + n3 + n4 + n5+ n6 + n7 + n8 + n9 + n10) ** 2
vahe = (ruutudesumma - summaruut)
vahe2 = (summaruut - ruutudesumma)
if summaruut < ruutudesumma:
    print("Summa erinevus on ", vahe)
else:
    print("Summa erinevus on ", vahe2)