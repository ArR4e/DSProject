def numbrikontroll(parool):
    täht = False
    number = False
    for i in parool:
        if i.isalpha():
            täht = True
        if i.isdigit():
            number = True
    if täht == True and number == True:
        return True
    else:
        return False

def paroolisisestus():
    global parool
    parool = input('Sisestage parool: ')
    global kontroll
    kontroll = input('Sisestage parool uuesti: ')

kasutajanimi = input('Sisestage kasutajanimi: ')
paroolisisestus()

while True:
    if parool != kontroll:
        print('\nSisestatud paroolid peavad omavahel kattuma.')
        paroolisisestus()
        continue
    elif len(parool) < 8:
        print('\nParool peab sisaldama vähemalt 8 tähemärki.')
        paroolisisestus()
        continue
    elif numbrikontroll(parool) == False:
        print('\nParool peab sisaldama nii tähti kui numbreid.')
        paroolisisestus()
        continue
    break

tagurpidi = parool[::-1]

f = open('users.txt', 'w')
print(kasutajanimi + ':' + tagurpidi, file = f)
f.close()