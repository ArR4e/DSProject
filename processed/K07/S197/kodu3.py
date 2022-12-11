def sünnikuupäev(isik):
    isik = list(map(int, list(isik))) #Eraldab numbrid järjendisse
    #Leiame kuupäeva
    day = f'{isik[5]}{isik[6]}'
    #Leiame kuu
    all_months = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    if isik[3] == 0:
        month = all_months[isik[4] - 1]
    if isik[3] == 1:
        month = all_months[isik[4] + 9]
    #Leiame aasta
    if isik[0] == 1 or isik[0] == 2:
        year = '18'
    if isik[0] == 3 or isik[0] == 4:
        year = '19'
    if isik[0] == 5 or isik[0] == 6:
        year = '20'
    if isik[0] == 7 or isik[0] == 8:
        year = '21'
    year += f'{isik[1]}{isik[2]}'
    return f'{day}. {month} {year}'