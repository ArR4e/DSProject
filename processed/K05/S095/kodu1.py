kasutajanimi=input("Sisesta kasutajanimi: ")
def numbertäht(paroolitest):
    test_1 = False
    test_2 = False
    for i in paroolitest:
        if i.isalpha():
            test_1 = True
        if i.isdigit():
            test_2 = True
    return test_1 and test_2
while True:
    parool=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if parool!=parool2:
        print("Paroolid ei kattu. Proovi uuesti")
    elif len(parool)<8:
        print("Parool liiga lühike. Proovi uuesti")
    elif numbertäht(parool)==False:
        print("Parool peab sisaldama tähti ja numbreid.")
    elif parool==parool2:
        break
def paroolipööre(x):
    return x[::-1]
parool=paroolipööre(parool)
with open('users.txt', 'a') as f:
    f.write('username: ')
    f.write(kasutajanimi)
    f.write('\n')
    f.write('password: ')
    f.write(parool)
    f.write('\n')
# print (kasutajanimi, parool)


# hea näide kuidas kontrollida kas tekst sisaldab numbrit ja tähte https://www.geeksforgeeks.org/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/
# hea näide sõne pööramisest https://www.w3schools.com/python/python_howto_reverse_string.asphttps://www.w3schools.com/python/python_howto_reverse_string.asp
# hea näide faili kirjutamisest https://www.pythontutorial.net/python-basics/python-write-text-file/
# et mitte üle kirjutada tekstifaili sisu https://stackoverflow.com/questions/22441803/how-to-write-to-a-file-without-overwriting-current-contents