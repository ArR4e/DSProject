kasutajanimi=input("Sisestage kasutajanimi: ")
f = open("users.txt","a" )
def registeerimisvorm():
    parool1= input ("Sisestage parool: ")
    parool2= input ("Sisestage parool uuesti: ")
    while parool1 == parool2:
        if len(parool1) < 8:
            print ("Sisestage pikem parool"), registeerimisvorm()
            
        if parool1.isalpha() == True:
            print ("Paroolis peavad olema nii tähed kui numbrid"), registeerimisvorm()
        
        if parool1.isnumeric() == True:
            print ("Paroolis peavad olema nii tähed kui numbrid"), registeerimisvorm()
        
        if parool1.isalnum() == False:
            print ("Paroolis peavad olema nii tähed kui numbrid"), registeerimisvorm()
        
        else:
            tagurpidi = parool1[::-1]
            print (tagurpidi)
            info = str(kasutajanimi) + ":" + str(tagurpidi) + "\n"
            f.write(info)
        return 
            
    else:
        print ("paroolid ei kattu"), registeerimisvorm()
    


registeerimisvorm()
f.close() 
