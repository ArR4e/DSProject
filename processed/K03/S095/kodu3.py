naturaalarv=int()
while naturaalarv<=0:
    naturaalarv=int(input("Sisesta Naturaalarv: "))
# print(naturaalarv)
# while naturaalarv>0:
#     naturaalarv-=1
#     print(naturaalarv)
summa=0
summaruut=0
ruutudesumma=0
while summa<naturaalarv:
    summa=summa+1
    summaruut+=summa
    ruutudesumma+=summa**2
    #print(summa)
summaruut=summaruut**2
#print(summaruut)
#print(ruutudesumma)
erinevus=summaruut-ruutudesumma
print("Summaruudu ja ruutude summa erinevus on: ", erinevus)

# while prinditud summade liitmisest sain abi: https://stackoverflow.com/questions/12082442/pythonhow-to-make-the-sum-of-the-values-of-a-while-loop-store-into-a-variable
    