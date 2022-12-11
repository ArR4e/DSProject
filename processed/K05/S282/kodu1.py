kasutajanimi=input('Sisestage kasutajanimi: ')
par=''

def parool():
    global par
    parool_1=input("Sisestage parool: ")
    parool_2=input("Korrake parooli: ")
    if parool_1==parool_2:
        par=parool_1
        pikkus()
    else:
        print("Paroolid ei kattu.")
        parool()



def pikkus():
    if len(par)<8:
        print("Parool peab olema vähemalt 8 tähemärki pikk.")
        parool()
    else:
        sisaldab()
        
        
def sisaldab():
    number=False
    taht=False
    for el in par:
        if el.isdigit():
            number=True
        elif el.isalpha():
            taht=True
    if number==True and taht==True:
        krypt()
    else:
        print("Parool peab sisaldama nii tähe- kui numbrimärke.")
        parool()
    
    
def krypt():
    par_uus=''
    pikk=len(par)
    for el in par:
        pikk-=1
        par_uus+=par[pikk]
    f=open("users.txt","w")
    f.write(kasutajanimi+':'+par_uus)
        
parool()