from math import ceil, floor

liin = input("Sisesta liini pikkus meetrites: ")
liin_pikkus = abs(int(liin))
post = input("Sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: ")
post_kaugus = abs(int(post))
post_amount = liin_pikkus / post_kaugus
jaak = liin_pikkus % post_kaugus
if jaak == 0:
    print("Liini ehitamiseks on minimaalselt vaja " + str(floor(post_amount)) + "." + " posti")
elif jaak != 0 and liin_pikkus >= post_kaugus:
    print("Liini ehitamiseks on minimaalselt vaja " + str(ceil(post_amount)) + "." + "posti")
else:
    print("Liini ehitamiseks on minimaalselt vaja 2. posti")
    


            
            
                
            
    
    