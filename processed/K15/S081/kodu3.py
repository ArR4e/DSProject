a = input('Sisestage failinimi: ')
fail = open(a, encoding='utf-8')


saabumisajad = []
for rida in fail:
    buss = rida.strip('\n').split(' ')
    saabumine = buss[1]
    s = saabumine.split(':')
    kell = int(s[0]), int(s[1])
    saabumisajad.append(kell)

madalaim = 0
for i in range(len(saabumisajad)):
    if i+1 < len(saabumisajad):
        if (saabumisajad[i][0] < saabumisajad[i+1][0] and saabumisajad[madalaim][0] > saabumisajad[i][0]) or (saabumisajad[i][0] == saabumisajad[i+1][0] and saabumisajad[i][1] < saabumisajad[i+1][1] and saabumisajad[madalaim][0] > saabumisajad[i][0]):
            madalaim = i


print('Kõige varem jõuab: ' + str(saabumisajad[madalaim][0]) + ':' + str(saabumisajad[madalaim][1]))
