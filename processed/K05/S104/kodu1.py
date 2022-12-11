input('Sisesta kasutajanimi: ')

parool1 = input('Sisesta parool: ')
parool2 = input('Korrake parooli: ')

def reverse_string(str):
    str1 = ''
    for i in str:
        str1 = i + str1
        return str1
    str = parool1

def lehekülg():
    if parool1 == parool2:
        tähti = len(parool1)
        if tähti > 8:
            str.isalpha(parool1)
            while True:
                return('Parool peab sisaldama numbreid ja sümboleid.')
            else:
                return('Kood tagurpidi on ', reverse_string(str))
        else:
            return('Tähti peab olema rohkem kui 8.')
    else:
        return('Paroolid pole samad.')

lehekülg()