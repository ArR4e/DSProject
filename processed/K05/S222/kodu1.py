def küsi():
    nimi = input("Sisesta kasutajanimi: ")
    parool = password()
    return nimi,parool
    
def password():
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    if parool1 != parool2:
        print("Paroolid ei kattu.")
        return password()
    elif parool1 == parool2:
        if len(parool1) < 8:
            print("Parool on liiga lühike.")
            return password()
        elif parool1.isalpha() or parool1.isnumeric(): #https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum/
            print("Paroolis peavad olema nii tähed kui numbrid.")
            return password()
        else:
            return parool1
    
def krüpto(parool):
    loorap = parool[::-1]
    return loorap

def kirjuta(login):
    nimi = login[0]
    parool = krüpto(login[1])
    fail = open("users.txt","a")
    fail.write(nimi+":"+parool+"\n")
    fail.close()
    
kirjuta(küsi())
    

