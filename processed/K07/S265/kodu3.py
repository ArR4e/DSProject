def sünnikuupäev(code):
    if int(code[0]) == 1 or int(code[0]) == 2:
        year = str(1800 + int(code[1] + code[2]))
    elif int(code[0]) == 3 or int(code[0]) == 4:
        year = str(1900 + int(code[1] + code[2]))
    elif int(code[0]) == 5 or int(code[0]) == 6:
        year = str(2000 + int(code[1] + code[2]))
    elif int(code[0]) == 7 or int(code[0]) == 8:
        year = str(2100 + int(code[1] + code[2]))
    else:
        year = 'error'
        print('valesti sisestatud isikukood')
    
    months = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    
    if int(code[3]+code[4])-1 != -1:
        month = months[int(code[3]+code[4])-1]
    else:
        month = 'error'
        print('valesti sisestatud isikukood')
    
    day = str(int(code[5]+code[6]))
    
    return day+'. '+month+' '+year