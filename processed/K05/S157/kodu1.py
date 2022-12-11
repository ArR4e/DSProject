def paroolnumbrid(parool): #vaatab kas paroolis on vahemalt uks taht ja uks number
    dig=0
    num=0
    for i in parool:
        if i.isalpha() == True:
            dig += 1
        elif i.isdigit() == True:
            num += 1
    if dig > 0 and num > 0:
        return True
    else:
        return False

def krupto(x): #peaks keerama parooli tagurpidi
    return x[::-1]

def fail(kasutaja,parool):
    f=open("users.txt","w+")
    f.writelines(kasutaja + ":" + parool)
    f.close() 
    

go= True
kasutaja=input("Sisesta kasutajanimi: ")
while go == True:
    
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta uuesti oma parool: ")
    if parool1 == "" or kasutaja == "":
        go=False
    else:
        if not parool1==parool2:
            print("Sisestatud paroolid peavad kattuma")
        else:
            'paroolpikkus(parool1)'
            if len(parool1) >= 8:
                paroolnumbrid(parool1) #vaatab kas paroolis on vahemalt uks taht ja uks number
                if paroolnumbrid(parool1)==True:
                    fail(kasutaja,krupto(parool1))
                    go= False
                    
                    
                else:
                    print("parool peab sisaldama v2hemalt yhte t2hte ja numbrit")
                        
            else:
                print("Parool peab olema v2hemalt 8 t2hte pikk")
                    
                
