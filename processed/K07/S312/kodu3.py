def sünnikuupäev(ik):
    kuud = [0, 'jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    sajand = 0
    sajandiindeks = ik[0]
    if sajandiindeks == '1' or sajandiindeks == '2':
        sajand = '18'
    elif sajandiindeks == '3' or sajandiindeks == '4':
        sajand = '19'
    else:
        sajand = '20'
    aasta = sajand + ik[1:3]
    kuu = int(ik[3:5])
    päev = str(int(ik[5:7]))
    kuunimi = kuud[kuu]
    return(päev + '. ' + kuunimi + ' '+ aasta)
    #'23. jaanuar 1945' 

