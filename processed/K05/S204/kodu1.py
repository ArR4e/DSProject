kasutajanimi=str(input("Palun sisesta endale sobilik kasutajanimi:"))
parool_1=str(input("Palun sisesta parool:"))
parool_2=str(input("Palun sisesta parool uuesti:"))


while parool_1==parool_2:
    #print("True 1")
    break
    
    
else:
    
    while not parool_1==parool_2:
        parool_1=str(input("Parool on puudulik, palun sisesta parool uuesti:"))
        parool_2=str(input("Palun sisesta parool uuesti:"))
        if parool_1==parool_2:
            break
        
  
while len(parool_1)>=8:
    #print("True 2")
    break
        
    

else:
    while len(parool_1)<=8:
        parool_1=str(input("Parool on puudulik, palun sisesta parool uuesti:"))
        parool_2=str(input("Palun sisesta parool uuesti:"))
        if parool_1==parool_2 and len(parool_1)>=8:
            break

for  i in parool_1:
    if((i.isalpha()) and not(i.isdigit())):
        #print("True 3")
        break
        
else:
    while not((i.isalpha() and not i.isdigit())):
        parool_1=str(input("Parool on puudulik, palun sisesta see uuesti:"))
        parool_2=str(input("Palun sisesta parool uuesti:"))
        if parool_1==parool_2 and len(parool_1)>=8 and not((i.isalpha()) and not(i.isdigit())):
            break
        
def reverse(parool_1):
    return parool_1[: : -1]
#print(reverse(parool_1))
    

print("Teie kasutajanimi on:",kasutajanimi)
print("Teie parool on:", reverse(parool_1))
