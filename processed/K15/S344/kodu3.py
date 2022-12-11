fail = open(input("Sisesta failinimi: "))
#fail = open("sõiduplaan.txt")

süidu_aeg_sobib = False
hind = False
suurem_summa = 0
väiksem_summa = 0

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

for rida in fail:
    rida = rida.split(" ")
    #print(rida)
    
    for rida in fail:
        for i in rida:
            if rida[0] < rida[1]:
                süidu_aeg_sobib = True
                #return True
            else:
                süidu_aeg_sobib = False
                #return False
    
    
    for rida in fail:
        for i in rida:
            if rida[2] > rida[2 + i]:
                hind = True
                print(hind)
                suurem_summa = int(rida[2])
            else:
                hind = False
                print(hind)
                väiksem_summa = int(hind + i)
            
    if süidu_aeg_sobib == True and hind == True:
        tulemus = rida.sort()
        print(tulemus)
    else:
        print("Sobivat tulemust ei leidu failis")
    
    
fail.close()
                
                



    
    

        
    
    