from math import ceil, floor

liin = round(float(input("Mis on liini pikkus meetrites?: ")))
vahe = round(float(input("Mis on elektripostide vahe?: ")))

#inputi positiivseks tegemine
if liin < 0:
    liin = liin * -1
else:
    liin = liin
if vahe < 0:
    vahe = vahe * -1
else:
    vahe = vahe

#postide arvutamine algne
#postid = liin // vahe + 1
#ule = liin % vahe
#if ule > 0:
    #print("Sul on vaja vahemalt ", postid + 1, " posti.")
#else:
    #print("Sul on vaja vahemalt ", postid, " posti.")
    
#postide arvutamine ceil'ga
postid = liin / vahe + 1
postid = ceil(postid)
print("Vaja on vahemalt ", postid, " posti.")



    