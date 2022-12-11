months = ['Jaanuar', 'Veebruar', 'Märts', 'Aprill', 'Mai', 'Juuni', 'Juuli', 'August', 'September', 'Oktoober', 'November', 'Detsember']

def sünnikuupäev(idnum: str):
    day = idnum[5:7]
    month = months[int(idnum[3:5])-1]
    year_2 = idnum[1:3]
    if int(idnum[0]) <= 2:
        year_1 = '18'
    elif int(idnum[0]) <= 4:
        year_1 = '19'
    else:
        year_1 = '20'
    year = year_1 + year_2
    
    return f'{day}. {month.lower()} {year}'

print(sünnikuupäev('50209112754'))
