aasta_kuud = ['tuhi','jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', """detsember"""]
def sünnikuupäev(kood):
    kood = [int(x) for x in str(kood)]
    paev = 10 * kood[5] + kood[6]
    kuu = aasta_kuud[10 * kood[3] + kood[4]]
    kumnend = 10 * kood[1]
    aasta = (kood[2])
    if kood[0] == 1 or kood[0] == 2:
        sajand = 18
    elif kood[0] == 3 or kood[0] == 4:
        sajand = 19
    elif kood[0] == 5 or kood[0] == 6:
        sajand = 20
    elif kood[0] == 7 or kood[0] == 8:
        sajand = 21
    if kood[1] == 0:
        return f"{paev}. {kuu} {sajand}{kumnend}{aasta}"
    return f"{paev}. {kuu} {sajand}{kumnend + aasta}"
print(sünnikuupäev(60101017683))