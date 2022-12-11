import re
nimi = str(input("Sisestage kasutaja nimi:"))

while True:
    parool1 = str(input("Seatke kontole parool:"))
    parool2 = str(input("Seatke konto parool uuesti:"))
    if parool1 == parool2:
        if len(parool1) >= 8:
            #kas sõnas on nii tähti kui ka numbreid
            #scr: https://www.tutorialspoint.com/How-to-check-if-a-string-has-at-least-one-letter-and-one-number-in-Python#:~:text=The%20easiest%20way%20to%20check%20this%20in%20python,and%20one%20number%2C%20we%20use%20re.match%20%28regex%2C%20string%29. 
            kontroll_2 = re.sub(r'[^\w\s]','',parool1)
            kontroll = bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', kontroll_2))
            if kontroll == True :
                #flipi parool
                parool1 = parool1[::-1]
                #ava fail kirjutamiseks
                f = open("users.txt","w+")
                #lisa lõppu kasutajanim:loorap
                f.write(nimi + ":" + parool1)
                f.close()
                break
            else:
                print("paroolis pole kasutatud vähemalt ühte tähte ja ühte numbrit")
                continue
        else:
            print("parool pole piisavalt pikk")
            continue
    else:
        print("Paroolid ei kattu, vigane parool")
        continue
