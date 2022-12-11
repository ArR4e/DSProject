def leia_sajand(number):
    if number in [1, 2]:
        return '18'
    elif number in [3, 4]:
        return '19'
    elif number in [5, 6]:
        return '20'
    elif number in [7, 8]:
        return '21'

def leia_kuu(number):
    if number == 1:
        return 'jaanuar'
    elif number == 2:
        return 'veebruar'
    elif number == 3:
        return 'märts'
    elif number == 4:
        return 'aprill'
    elif number == 5:
        return 'mai'
    elif number == 6:
        return 'juuni'
    elif number == 7:
        return 'juuli'
    elif number == 8:
        return 'august'
    elif number == 9:
        return 'september'
    elif number == 10:
        return 'oktoober'
    elif number == 11:
        return 'november'
    elif number == 12:
        return 'detsember'
    
def sünnikuupäev(isikukood):
    sajand = leia_sajand(int(isikukood[0]))
    aasta = sajand + isikukood[1:3]
    kuu = leia_kuu(int(isikukood[3:5]))
    päev = isikukood[5:7]
    return f'{int(päev)}. {kuu} {aasta}'
    