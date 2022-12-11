kuud = ("jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember")
isikukood = input("Sisetage isikukood: ")


if isikukood[0] in ("3","4"):
    aasta = 1900
if isikukood[0] in ("5","6"):
    aasta = 2000
kümmend = int(isikukood[1:3])
aasta += kümmend


kuu = int(isikukood[3:5])
päev = int(isikukood[5:7])
print (str(päev)+ ".", kuud[kuu-1],aasta)

