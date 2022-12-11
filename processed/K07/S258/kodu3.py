def sünnikuupäev(kood):
    aasta=""
    if kood[0] in ["1","2"]:
        aasta="18"+kood[1:3]
    elif kood[0] in ["3","4"]:
        aasta="19"+kood[1:3]
    elif kood[0] in ["5","6"]:
        aasta="20"+kood[1:3]
    elif kood[0] in ["7","8"]:
        aasta="21"+kood[1:3]
    return str(int(kood[5:7]))+". "+kuud[int(kood[3:5])-1]+" "+aasta
kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]