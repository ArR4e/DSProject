def võrdle(esimene, teine):
    ajad1 = esimene.split(" ")
    ajad2 = teine.split(" ")
    if int(ajad2[0].replace(":", "")) < int(ajad1[0].replace(":", "")):
        if int(ajad2[1].replace(":", "")) > int(ajad1[1].replace(":", "")):
            if int(ajad2[2].replace(":", "")) > int(ajad1[2].replace(":", "")):
                return teine
    return 0
    
    
def järjesta(bussiajad):
    for i in range(len(bussiajad)):
        for j in range(len(bussiajad)):
            if i != j:
               if int((bussiajad[i].split(" ")[0]).replace(":", "")) < \
                  int((bussiajad[j].split(" ")[0]).replace(":", "")):
                   bussiajad[i], bussiajad[j] = bussiajad[j], bussiajad[i]

        
    
failinimi = input("Sisesta failinimi: ")
f = open(failinimi, "r", encoding = "UTF-8")
bussid = f.readlines()
for i in range(len(bussid)):
    bussid[i] = bussid[i].strip()

uus_list = []

for i in range(len(bussid)):
    for j in range(len(bussid)):
        if i != j: 
            if võrdle(bussid[i],bussid[j]) != 0:
                uus_list.append(võrdle(bussid[i],bussid[j]))


bussid = set(bussid)
uus_list = set(uus_list)
vastus = list(bussid - uus_list)
järjesta(vastus)
for el in vastus:
    print(el)
f.close()
                





    

