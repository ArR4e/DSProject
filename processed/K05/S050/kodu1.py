
kasutajanimi=input("Sisesta kasutajanimi: ")
while True:
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta parool: ")
    
    if parool1==parool2:
        True
    else:
        print('Paroolid ei kattu.')
        continue
    
    
    if len(parool1)>=8:
        True
    else:
        print('Parool on vähem kui 8 tähemärki.')
        continue
    kasOnNumber = False
    for character in parool1:
        if character.isdigit():
            kasOnNumber= True
            break
    if kasOnNumber:
        True
    else:
        print('Paroolis ei ole numbrit.')
        continue
    kasOnTäht = False
    for character in parool1:
        if character.isalpha():
            kasOnTäht= True
            break
    if kasOnTäht:
        True
        break
    else:
        print('Paroolis ei ole tähti.')
        continue
 
tulemus=kasutajanimi+':'+parool1[::-1]
f = open("users.txt", "w")
f.write(str(tulemus))
f.close()



# print (kasutajanimi, ":" ,parool1[::-1])


