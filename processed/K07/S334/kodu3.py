kuud = ['', 'jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
def sünnikuupäev(n):
    if int(n[0]) == 1 or int(n[0]) == 2:
        return '%s. %s 18%s' %(n[5:7], kuud[int(n[3:5])], n[1:3])
    elif int(n[0]) == 3 or int(n[0]) == 4:
        return '%s. %s 19%s' %(n[5:7], kuud[int(n[3:5])], n[1:3])
    else:
        return '%s. %s 20%s' %(n[5:7], kuud[int(n[3:5])], n[1:3])
print(sünnikuupäev('60101017683')) # 23 jaanuar 1945