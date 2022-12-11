while True:
    kasutajanimi = input("Sisestage kasutajanimi ")
    parool = input("Sisestage parool ")
    uuesti = input("Sisestage parool uuesti ")
    if parool == uuesti :
        if len(parool) >= 8:
            if not str.isalpha(parool) and not parool.isdigit():
                tagurpidi = (parool[::-1])
                f = open("users.txt", "w")
                f.write(kasutajanimi + ":" + tagurpidi)
                f.close()
                break
            else :
                print("midagi läks valesti")
                continue 
        else :
            print("midagi läks valesti")
            continue 
    else :
        print("midagi läks valesti")
        continue 
            
            
            

