nimi = input('Sisesta kasutajanimi:')
x = input('Sisesta parool:')
y = input('Sisesta parool:')
def sobib(parool1, parool2):
    number = 0
    täht = 0
    if parool1 != parool2:
        print('Paroolid ei kattu, proovi uuesti!')
        return False
    if len(parool1) < 8:
        print('Parool peab sisaldama vähemalt 8 tähemärki!')
        return False
    for i in parool1:
        if i.isalpha():
            täht = 1
        if i.isdigit():
            number = 1
    if number != 1 or täht != 1:
        print('Paroolis peab olema numbreid ja tähti, proovi uuesti!')
        return False        
    else:
        return True
while sobib(x, y) == False:
    x = input('Sisesta parool:')
    y = input('Sisesta parool:')
parool = x[::-1]
f = open('users.txt', 'w')
f.write(nimi + ':' + parool)
f.close()