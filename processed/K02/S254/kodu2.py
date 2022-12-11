#Sirgjjonelised elektriliinid
"""
1. Kõrvutiasetsevad postid on võrdsete kaugustega. OK
2. Ei tohi ületada etteantud maksimaalkaugust. 
3. Liin algab ja lõppeb postiga OK
"""
import math
liini_pikkus = int(input("Sisestage liini pikkus meetrites, täisarvuna: "))
postide_max_kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites, täisarvuna: "))


postide_arv = int(math.ceil(liini_pikkus / postide_max_kaugus) + 1)

print("Liini ehitamiseks on minimaalselt vaja " + str(postide_arv) + " posti.")