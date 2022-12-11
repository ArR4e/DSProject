failinimi = input("Sisestage faili nimi:")
fail = open(failinimi, 'r')
andmed = fail.readlines()
andmed2 = [tuple(line.strip().split(' ')) for line in andmed]
eisobi = []
sobivad = []


# leian ajad, mis ei sobi
for i in range(len(andmed2)):
    for j in range(len(andmed2)):
        if andmed2[i][0] < andmed2[j][0] and andmed2[i][1] > andmed2[j][1] and float(andmed2[i][2]) > float(andmed2[j][2]):
            eisobi.append(andmed2[i])
            
## eemaldan ajad mis ei sobi
for element in andmed2:
    if element in eisobi:
        pass
    else:
        sobivad.append(element)
        

sobivad.sort()


print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for element in sobivad:
    print(element[0], element[1], element[2])

        
            

   
    

    
   

    