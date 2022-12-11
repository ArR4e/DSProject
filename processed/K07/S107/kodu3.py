kuud = ("jaanuar","veebruar","märts","aprill","mai","juuni",
           "juuli","august","september","oktoober","november","detsember")

isikukood = input("Sisesta isikukood: ")
def sünnikuupäev(isikukood):

    #sünniaasta
    if isikukood[0] == "1" or isikukood[0] == "2":
        sünniaasta = 1800
    if isikukood[0] == "3" or isikukood[0] == "4":
        sünniaasta = 1900
    if isikukood[0] == "5" or isikukood[0] == "6":
        sünniaasta = 2000
    #võtab isikukoodist 2. ja 3. numbri ning liidab need vastavale sünniaastale.        
    aastad = int(isikukood[1:3])
    sünniaasta += aastad
    sünnikuu = int(isikukood[3:5]) #kuu, võtab isikukoodist 4. ja 5. numbri
    sünnipäev = int(isikukood[5:7]) #päev, võtab isikukoodist 6. ja 7. numbri.


    print(str(sünnipäev)+".",str(kuud[sünnikuu-1]), str(sünniaasta))
sünnikuupäev(isikukood)