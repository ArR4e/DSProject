import re
nimi=input('Sisestage kasutajanimi: ')
parool1=input('Sisestage kasutaja parool: ')
parool2=input('Sisestage uuesti kasutaja parool: ')

def sisaldabnumbrit(parool1):
    for i in parool1:
        if i.isdigit():
            return True
    return False
def sisaldabtahti(parool1):
    for i in parool1:
        if i.isalpha():
            return True
    return False
while True:
    if parool1==parool2:
        if len(parool1) >=8:
            if sisaldabtahti(parool1):#parool1 in bool(re.search('[a-zA-Z]+',parool1)):
                if sisaldabnumbrit(parool1):
                    parool=parool1[::-1]
                    f = open("user.txt", "w")
                    f.write(nimi + '\n' + parool1 + '\n')
                    f.close()
                    break

    print('Paroolid ei ühti')
    parool1=input('Sisestage kasutaja parool: ')
    parool2=input('Sisestage uuesti kasutaja parool: ')        
#kirjuta fail kuhu tuleb kasutajanimi ja parool (user.txt) ja kasutajanimi loorap    