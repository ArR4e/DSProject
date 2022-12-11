def sünnikuupäev(a):
    aastalõpp = a[1]+a[2]
    kuunr = int(a[3]+a[4])-1
    päevnr = a[5]+a[6]
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    
    if int(a[0]) == 5 or int(a[0]) == 6:
        sajand = '20'
    elif int(a[0]) == 3 or int(a[0]) == 4:
        sajand = '19'
    else:
        sajand = '18'
    sünnipäev = päevnr + '. ' + kuud[kuunr] + ' ' + sajand + aastalõpp
    return (sünnipäev)
    
    
print(sünnikuupäev('49812238394'))