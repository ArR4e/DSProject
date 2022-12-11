import re
with open('aadressid.txt', encoding = "UTF-8") as kasutaja:
    print("Kasutajanimed on: ")
    for i in kasutaja:
        nimi = i.strip("http://")    # D
        nimi = nimi + '/'
        nimi1 = re.search("www.ut.ee/~(\w+)/",  nimi)
        if nimi1:
            print(nimi1.group(1))

                
