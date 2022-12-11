knimi = input("sisesta kasutajanimi :")

while True:
    par1 = input("sisesta parool: ")
    par2 = input("sisesta parool uuesti:" )

    if par1 != par2:
        print("paroolid peavad kattuma")
    else:
        if len(par1) < 8:
            print("parool peab olema vähemalt 8 tähemärki pikk")
        else:
            if not par1.isalpha() and not par1.isdigit() == True:
                par1 = par1[::-1]
                break
            else:
                print("paroolis peab olema kastutatud nii tähti kui numbreid")
                
    
f = open("users.txt", "w")
f.write(knimi + ":" + par1)

# 1#a$b!4%
# par1.isalnum()
f.close()