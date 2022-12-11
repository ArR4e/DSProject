aasta_tulu = float(input('Sisesta oma aastatulu eurodes: '))
arv = aasta_tulu

round(vastus, 2)

if arv > 0 and <= 6000:
    print('Maksuvaba tulu on võrdne sissetulekuga.')
elif arv > 6000 and <= 14400:
    print('Maksuvaba tulu on 6000 eurot aastas.')
elif arv > 14400 and <= 25200:
    vastus = (6000 - 6000/10800*(arv - 14400))
    print('Maksuvaba tulu on ' + vastus + 'eurot aastas.')
elif arv > 252000:
    print('Maksuvaba tulu on 0 eurot aastas.')
else print('Sissetulek ei saa olla negatiivne... ')
