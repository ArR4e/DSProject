def sünnikuupäev(isikukood):
    järjend = list(isikukood)
    if järjend[3]=='0':
        kuu = int(järjend[4])
    else:
        kuu = int(järjend[3]+järjend[4])
    if järjend[0]=='3' or järjend[0]=='4':
        aasta = '19'+järjend[1]+järjend[2]
    elif järjend[0]=='2' or järjend[0]=='1':
        aasta = '18'+järjend[1]+järjend[2]
    else:
        aasta = '20'+järjend[1]+järjend[2]
    return järjend[5]+järjend[6]+'. '+kuud[kuu]+' '+aasta
        

kuud=['', 'jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli',
      'august', 'september', 'oktoober', 'november', 'detsember']