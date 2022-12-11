from math import*

liini_pikkus= int(input("Sisestage liini pikkus (täisarvuna meetrites): "))
#täisarvuna meetrites

postidevaheline_kaugus_maks=int(input("Kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
#Postidevaheline_kaugus=50
#kõrvutiasetsevate postide maksimaalkaugust (täisarvuna meetrites)
postide_arv=ceil((liini_pikkus/postidevaheline_kaugus_maks)+1)
#postid_2=int((liini_pikkus/50)+1)

print(postide_arv)



#if liini_pikkus>postidevaheline_kaugus_maks :
   # print("Liini ehitamiseks läheb vaja "+str(postide_arv)+". posti.")
#elif postidevaheline_kaugus_maks>50 :
    #print(postid_2)
#elif postidevaheline_kaugus_maks==liini_pikkus :
    #print("Liini ehitamiseks läheb vaja "+str(2)+". posti.")
#elif liini_pikkus<postidevaheline_kaugus_maks :
    #print("Liini ehitamiseks läheb vaja "+str(1)+". posti.")
    
    
    

