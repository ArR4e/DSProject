nimi=input("Sisesta oma kasutajanimi")


while True:
    parool1=input("Sisesta oma parool")
    parool2=input("Sisesta oma parool uuesti")
    
    if parool1 != parool2:
        print("Paroolid ei kattu")
        continue
    
    if len(parool1) < 8:
        print("Parool on liiga lühike")
        
    täht=False
    number=False
    for x in parool1:
        if x.isalpha():
            täht=True
        if x.isnumeric():
            number=True
        if täht and number:
            pass
    if täht==False and number==False:
        print("Paroolis peavad olema tähed ja numbrid")
    
    
    break
    
parool=parool1[::-1]
print(parool)

fail=open("users.txt", "w")
fail.write(nimi+":")
fail.write(parool)
fail.close

    
    