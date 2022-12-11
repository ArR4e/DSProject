nimi=input("Sisesta kasutajanimi: ")

def kt(p1):
    for i in p1:
        if i.isdigit():
            return True
    return False

def kd(p1):
    for i in p1:
        if i.isalpha():
            return True
    return False

def main():
    p1=input("Sisesta parool: ")
    p2=input("Sisesta parool uuesti: ")
    if p1 == p2:
        if len(p1) >= 8:
            if kt(p1) == True and kd(p1) == True:
                uusp1 = p1 [::-1]
                f= open("users.txt", "w")
                f.write(nimi + ":" + uusp1)
                f.close()
            else:
                return False
        else:
            return False
    else:
        return False
      
while main() == False:
    print("proovi uuesti")
    
