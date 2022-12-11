import string
nimi = input("Sisesta kasutajanimi: ")
numbrid = set(list(string.digits))
tähed = set(list(string.ascii_letters))

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
    if parool2 != parool1:
        print("Paroolid ei kattu. Sisesta uuesti.")
        continue
    
    if len(parool2) < 8:
        print("Parool peab olema vähemalt 8 tähemärki.")
        continue
    
    tähemärgid = set(list(parool2))
    
    if not numbrid.intersection(tähemärgid):
        print("Parool peab sisaldama nii tähti kui ka numbreid.")
        continue
    if not tähed.intersection(tähemärgid):
        print("Parool peab sisaldama nii tähti kui ka numbreid.")
        continue
    #https://stackoverflow.com/questions/41941421/how-to-check-the-password-for-numbers-in-python
    break

parool_lõpp = (parool2[::-1])
#https://www.w3schools.com/python/python_howto_reverse_string.asp
fail = open("users.txt", "a")
fail.write(nimi + ":" + parool_lõpp + "\n")
fail.close()

