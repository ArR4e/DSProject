import re
f=open("aadressid.txt", "r", encoding="UTF-8")
print("Kasutajanimed on:")
for rida in f:
    rida=rida.strip()
    if re.match("http.*://www.ut.ee/", rida):
        #print("UT aadress")
#         muutuja=re.search("(~.*)", rida)
#         print(muutuja.groups())
        if re.search("(~.*)", rida):
            rida_list=rida.split("/")
            pikkus=len(rida_list)
            #print(rida_list, pikkus)
            nimi=rida_list[3]
            nimi2_list=list(nimi)
            nimi2="".join(nimi2_list[1:])
            print(nimi2)
f.close()
