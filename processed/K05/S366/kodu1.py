nimi = input("Sisestage kasutajanimi: ")
def reverse(parool):
    parool = parool[::-1]
    return parool




while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")

    if parool1 == parool2:
        if len(parool1) >= 8:
            if parool1.isalnum() == True:
                parooluus = reverse(parool1)
                #print(parooluus)
                f = open("users.txt", "w")
                f.write(nimi + ":" + parooluus)
                f.close()
                break
            
    else:
        continue


    
    

        