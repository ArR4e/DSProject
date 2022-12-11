# failinimi=input("Sisesta failinimi: ") #bussiplaan_hind.txt
# f=open(failinimi, "r", encoding="UTF-8")
# sisu=f.readlines()
# f.close()
# listide_list=[]
# for rida in sisu:
#     rida=rida.strip().split(" ")
#     listide_list+=[rida]
# #print(listide_list)
# for i in range(len(listide_list)):
#     for j in range(i+1,len(listide_list)):
#         if listide_list[i][2]>listide_list[j][2]:
#             listide_list[i],listide_list[j]=listide_list[j],listide_list[i]
# #print(listide_list)
# uus_list=listide_list[:(len(listide_list)-1)]
# #print(uus_list)
# for i in range(len(uus_list)):
#     for j in range(i+1,len(uus_list)):
#         if uus_list[i][1]>uus_list[j][1]:
#             uus_list[i],uus_list[j]=uus_list[j],uus_list[i]
# #print(uus_list)
# uus_list2=uus_list[:(len(uus_list)-1)]
# #print(uus_list2)
# print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
# for el in uus_list2:
#     print(" ".join(el))
##VER2##    
failinimi=input("Sisesta failinimi: ") #bussiplaan_hind.txt
f=open(failinimi, "r", encoding="UTF-8")


listide_list=[]
uus_list=[]
uus_list2=[]
for rida in f:
    rida=rida.strip().split(" ")
    listide_list+=[rida]
#print(listide_list)
for i in range(len(listide_list)):
    sobivus=True
    for j in range(len(listide_list)):
        if listide_list[i][2]>listide_list[j][2] and  listide_list[i][0]<listide_list[j][0] and listide_list[i][1]>listide_list[j][1]:
#             print(listide_list[i])
#             print(listide_list[j])
            sobivus=False
    
#         elif listide_list[i][2]<listide_list[j][2] and listide_list[i][0]>listide_list[j][0] and listide_list[i][1]<listide_list[j][1] :
#             sobivus=True
    if sobivus==True:
        uus_list+=[listide_list[i]]

for i in range(len(uus_list)):
    for j in range(i+1, len(uus_list)):
        if uus_list[i][0]>uus_list[j][0]:
            uus_list[i],uus_list[j]=uus_list[j],uus_list[i]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for el in uus_list:
    print(" ".join(el))
    
    