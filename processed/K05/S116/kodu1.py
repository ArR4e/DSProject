kn = input("Sisesta kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
    if parool1 != parool2:
        print("Paroolid ei klapi!")
        continue
    
    if len(parool1) < 8:
        print("Parool on liiga lühike!")
        continue
    
    nr = 0
    täht = 0
    for i in parool1:
        if i.isdigit():
            nr += 1
        if i.isalpha():
            täht += 1
        
    if nr == 0 or täht == 0:
        print("Parool peab sisaldama nii tähti kui numbreid!")
        continue
    
    break



loorap = parool1 [::-1]

fail = open("users.txt", "w")
fail.write(kn)
fail.write(":")
fail.write(loorap)
fail.close()



