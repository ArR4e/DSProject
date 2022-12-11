def keera_pass(pass_):
    pass_list = list(pass_)
    ssap_list = pass_list[::-1]
    ssap = ""
    for element in ssap_list:
        ssap += element
    return ssap

def kirjuta_pass_faili(user, pass_):
    f = open("users.txt", "a")
    f.write(user + ":" + pass_ + "\n")
    f.close()


username = input("Kasutajanimi: ")


while True:
    pass1 = input("Parool: ")
    pass2 = input("Parool teist korda: ")
    
    if pass1 == pass2:    #---------1.Tingimuse kontroll
        
        if len(pass1) >= 8:    #---------2.Tingimuse kontroll
            
            numbrid = list(range(10))
            tahed = list("qwertyuiopasdfghjklzxcvbnmüõöäQWERTYUIOPASDFGHJKLZXCVBNMÜÕÖÄ")
            number_on = False
            taht_on = False
            
            for number in numbrid:
                number_str = str(number)
                if number_str in pass1:
                    number_on = True
                    
            for taht in tahed:
                if taht in pass1:
                    taht_on = True
            
            if taht_on and number_on:    #---------3.Tingimuse kontroll
                ssap1 = keera_pass(pass1)
                kirjuta_pass_faili(username, ssap1)
                break
            
            else:
                print("Parool peab sisaldama nii tähti kui ka numbreid. Proovi uuesti.")
            
        else:
            print("Parool peab olema vähemalt 8 sümbolit pikk. Proovi uuesti.")
    else:
        print("Teist korda sisestatud parool ei klapi esimest korda sisestatud parooliga. Proovi uuesti.")
