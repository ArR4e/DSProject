liini_pikkus = int(input("Liini pikkus on: "))
max_kaugus = int(input("Postide maksimaalkaugus on: "))

min_postid = liini_pikkus // max_kaugus + 2 #Lisandub 2 otsa posti

if max_kaugus == 1:
    min_postid -= 1
if liini_pikkus == max_kaugus:
    min_postid = 2

print("Liini ehitamiseks on minimaalselt vaja", str(min_postid), "posti.")