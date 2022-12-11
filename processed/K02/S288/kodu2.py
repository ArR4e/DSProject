liin = int(input('Sisestage elektriliini pikkus: '))
post = int(input('Sisestage postide kaugus üksteisest: '))

tulemus = int(liin / post) + 2

print('\n', '\n')
if liin == post:
    print('Minimaalselt on elektriliini ehitamiseks vaja 2 posti.')
if post == liin / 2:
    print('Minimaalselt on elektriliini ehitamiseks vaja', int(tulemus / tulemus + 2), 'posti.')
else:
    print('Minimaalselt on elektriliini ehitamiseks vaja', tulemus, 'posti.')