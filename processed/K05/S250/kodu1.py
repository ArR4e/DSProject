nimi = input("Kasutajanimi: ")

def sisaldabNumbreid(parool):
    if True in [tmärk.isnumeric() for tmärk in parool]:
        return True
    return False

def sisaldabTähti(parool):
    if True in [tmärk.isalpha() for tmärk in parool]:
        return True
    return False

while True:
    global parool1
    parool1 = input("Parool: ")
    parool2 = input("Parool (kontroll): ")
    if parool1 != parool2:
        print('Viga! Sisestatud paroolid on erinevad.')
        continue
        
    if len(parool1) < 8:
        print('Viga! Sisestatud parool peab olema pikem kui 8 tähemärki.')
        continue
        
    if sisaldabNumbreid(parool1) == False or sisaldabTähti(parool1) == False:
        print('Viga! Sisestatud parool peab sisaldama nii tähti kui numbreid.')
        continue
    else:
        parool_tagurpidi = parool1[::-1]

        fail = open('users.txt', 'w')
        fail.write(str(nimi) + ':' + str(parool_tagurpidi))
        fail.close()
        break






    