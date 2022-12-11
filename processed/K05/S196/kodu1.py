kasutajanimi = input("Sisesta kasutajanimi: ")

#sain meetodi sõnes tähtede ja numbrite kontrollimiseks siit:
#https://stackoverflow.com/questions/64862663/how-to-check-if-a-string-is-strictly-contains-both-letters-and-numbers
def tähedjanumbrid(a):
    täht = False
    number = False
    for x in a:
        if x.isalpha():
            täht = True
        elif x.isnumeric():
            number = True
        if täht == True and number == True:
            return True
    return False

while True:
    parool = input("Sisesta parool: ")
    paroolikontroll = input("Sisesta parool uuesti: ")
    if parool == paroolikontroll:
        if len(parool) >= 8:
            if tähedjanumbrid(parool) == True:
                break
            else:
                print("Parool peab sisaldama nii tähti kui numbreid")
        else:
            print("Parool on liiga lühike")
    else:
        print("Paroolid ei kattu")
        
def pööra_tagurpidi(sõna):
    sõna_pikkus = len(sõna) - 1 #sest algab 0st
    uus_sõna = ""
    while sõna_pikkus >= 0:
        täht = sõna[sõna_pikkus]#või number
        uus_sõna = uus_sõna + täht
        sõna_pikkus -= 1
    return uus_sõna
        
tagurpidi_parool = pööra_tagurpidi(parool)

f = open("users.txt", "w")
f.write(kasutajanimi + ":" + tagurpidi_parool)
f.close()