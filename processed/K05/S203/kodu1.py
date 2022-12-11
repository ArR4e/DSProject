import re
kasutaja = input("Sisestage kasutajanimi: ")


while True:
    par1 = input("Sisestage parool: ")
    par2 = input("Sisestage parool uuesti: ")
    if par1 == par2:
        parooli_pikkus = len(par1)
        if parooli_pikkus >= 8:
            on_arv = re.findall("[0-9]", par1)
            numbrid = len(on_arv)
            if len(on_arv) > 0:
                if len(par1) > len(on_arv):
                    tagurpidi = par1 [::-1]
                    fail = open("users.txt", 'w')
                    fail.write(str(kasutaja) + ":" + str(tagurpidi))
                    fail.close()
                    break
                else:
                    print("Parool ei sisalda tähti")
            else:
                print("Parool ei sisalda numbreid")
        else:
            print("Parool ei ole piisavalt pikk")
    else:
        print("Paroolid ei ole samad, palun sisestage uuesti")


