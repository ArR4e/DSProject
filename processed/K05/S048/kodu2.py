kasutajanimi = input("Sisestage oma kasutajanimi ")

while True:
    parool = input("Sisestage oma parool. ")
    parool_2 = input("Sisestage oma parool uuesti. ")
    if parool == parool_2:
        if len(parool) >= 8:
            if kontrolli_parooli(parool):
                break
            else:
                print("Parool ei sobi! Parool peab sisaldama nii tähti kui ka numbreid!")
        else:
            print("Parool pole piisavalt pikk! Parool peab olmea 8 märki pikk!")
    else:
        print("Paroolid ei ole samad!")

parooli_tähtede_list = list(parool)
parooli_tähtede_list.reverse()
parool_tagurpidi = "".join(parooli_tähtede_list)


with open("users.txt", mode="a") as fail:
    fail.write(kasutajanimi + ":" + parool_tagurpidi)