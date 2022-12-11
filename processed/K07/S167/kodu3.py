#sünnikuupäev

#id = "34501234215"
#>>> sünnikuupäev('34501234215')
#'23. jaanuar 1945'

#list

#aasta (3 = 1900.1999.a sündinud mees)
def sünnikuupäev(id):
    
    list = []
    for i in id:
        list.append(i)
    
    def sünniaasta():
        sünniaasta = ""
        i = 0
        while i < 1:
            d = str(list[i])
            sünniaasta += d
            if d == "1":
                sünniaasta = "18"
            if d == "2":
                sünniaasta = "18"
            if d == "3":
                sünniaasta = "19"
            if d == "4":
                sünniaasta = "19"
            if d == "5":
                sünniaasta = "20"
            if d == "6":
                sünniaasta = "20"
            i += 1
        while i<3:
            d = str(list[i])
            sünniaasta += d
            i += 1
        return sünniaasta
    print(sünniaasta())

    def kuu():
        sünnikuu = ""
        i = 3
        while i < 5:
            d = str(list[i])
            sünnikuu += d
            i += 1
            list3 = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
        list2 = []
        for i2 in sünnikuu:
            list2.append(i2)
        if list2[0] == "0":
            sünnikuu = list2[1]
        kuu = list3[int(sünnikuu)-1]
        return kuu

    def päev():
        sünnipäev = ""
        i = 5
        while i < 7:
            d = str(list[i])
            sünnipäev += d
            i += 1
        sünnipäev = sünnipäev + "."
        return sünnipäev
    sünnikp = päev() + " " + kuu() + " " + sünniaasta()
    return sünnikp
print(sünnikuupäev("34501234215"))