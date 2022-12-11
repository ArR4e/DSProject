
kasutajan = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 =input("Sisesta uuesti parool: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if parool1.isalpha()==False and parool1.isnumeric()==False:
                break
            else:
                print("Parool peab sisaldama tähti ja numbreid. Vali uus parool.")   
        else:
            print("Parool on liiga lühike. Vali uus parool")
    else:
        print("Paroolid ei ole samasugused. Proovi uuesti.")

def parool_tagurpidi(parool):
    tagurpidi_parool = ""
    i = len(parool)
    while i:
        i -= 1
        tagurpidi_parool += parool[i]
    return tagurpidi_parool

#print(parool_tagurpidi(parool1))

tagurpidi = parool_tagurpidi(parool1)
fail = open("users.txt", "w")
fail.write(kasutajan+":"+tagurpidi)
fail.close()