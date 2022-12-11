kasutajanimi = str(input("Sisesta oma kasutajanimi: "))
def string(x):
    flag_l = False
    flag_n = False
    for i in (x):
        if i.isalpha():
            flag_l=True
        if i.isdigit():
            flag_n=True
    return flag_l and flag_n
while True:
    parool = str(input("Sisesta soovitud parool esimest korda: "))
    parool2 = str(input("Sisesta soovitud parool teist korda: "))
    if parool != parool2:
        print("Paroolid ei klapi!")
        continue
    elif parool == parool2:
        if len(parool) >= 8:
            if string(parool) == True:
                tagurpidi=parool[::-1]
                
                print("Tubli")
                break
            else:
                print("Paroolis peab olema vähemalt 1 tähemärk ja 1 numbrimärk")
                continue
        else:
            print("Parool on liiga lühike")
            continue
f=open("users.txt","w")
L=kasutajanimi+":"+tagurpidi
f.write(L)
f.close()
