kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool teist korda: ")
    if parool1 != parool2:
        print("Esimene ja teine parool peavad ühtima")
        
        
    while parool1 == parool2:
        pass
        if len(parool1) >= 8:
            pass
        else:
            print("Sõne peab olema vähemalt 8 tähemärki pikk")
            break
        
        on_täht = False
        on_number = False
        for x in parool1:   
            if x.isalpha():
                on_täht = True
            if x.isnumeric():
                on_number = True
            if on_täht and on_number:
                pass
            
        if on_täht == False and on_number == False or on_täht == True and on_number == False or on_täht == False and on_number == True:
            print("Sõnes pole kasutatud nii tähti kui numbreid")
            break
        if on_täht and on_number:
            break
    if on_täht and on_number:                   #kui paroolis on täidetud kõik tingimused tuleb väljuda while ja while True tsüklist
        break
        
    
parool = parool1 = parool2
pikkus = len(parool)
tagurpidiparool = parool[pikkus::-1]
fail = open('users.txt', 'w')
fail.writelines(kasutajanimi + ':' + tagurpidiparool)
fail.close()

        
    

            
        
        
    


    
    
    