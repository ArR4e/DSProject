import sys
import re

def parool1(a, b):
    if a == b:
        return True
    else:
        print("Palun kirjutage kasutajanimi ning parool uuesti.")
        sys.exit()
        
def parool2(a):
    if len(a) >= 8:
        return True
    elif len(a) < 8:
        print("Palun kirjutage kasutajanimi ning parool uuesti.")
        sys.exit()
        
def parool3(a):
    if re.search('[0-9]',a) is None:
        print("Palun kirjutage kasutajanimi ning parool uuesti.")
        sys.exit()
    elif re.search('[a-z]',a) is None and re.search('[A-Z]',a) is None:
        print("Palun kirjutage kasutajanimi ning parool uuesti.")
        sys.exit()
    else:
        return True

print("Palun kirjutage oma kasutajanimi ja sisestage oma parool kaks korda.")
print("Esimene parool peab kattuma teise parooli. See peab sisaldama vähemalt 8 tähemärki ja sisaldama nii numbreid kui ka tähti.")

kasutajanimi = input("Palun kirjutage oma kasutajanimi: ")
esimene_parool = input("Palun sisestage oma parool: ")
teine_parool = input("Palun sisestage uuesti oma parool: ")

parool1(esimene_parool, teine_parool)
parool2(esimene_parool)
parool3(esimene_parool)

loorap = esimene_parool[::-1]

with open('users.txt', 'w') as file:
    file.write(kasutajanimi + ":" + loorap)
    


print("...")
