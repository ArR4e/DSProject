def pööra(parool):
    pikkus = len(parool)
    pööratud = [' '] * pikkus
    i = 1
    for letter in parool:
        if i > pikkus:
            break
        pööratud[-i] = letter
        i += 1
    str = ''
    for element in pööratud:
        str += element
    return str

kasutajanimi = input("Sisesta kasutajanimi: ")
while True:
    parool_1 = input("Sisesta parool: ")
    parool_2 = input("Sisesta parool veel kord: ")
    for i in parool_2:
        if i.isdigit():
            bool_1 = True
            break
        else:
            bool_1 = False
    for i in parool_2:
        if i.isalpha():
            bool_2 = True
            break
        else:
            bool_2 = False
    if parool_2 == parool_1 and len(parool_1) >= 8 and (bool_1 and bool_2):
        break
    

fail = open("users.txt", 'w')
fail.write(kasutajanimi + ":" + pööra(parool_2))
fail.close()
        