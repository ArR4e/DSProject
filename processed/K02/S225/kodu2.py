from math import ceil
pikkus = int(input('Sisestage liini pikkus(täisarv): '))
postidevahe = int(input('Sisestage postidevaheline kaugus(täisarv): '))

postid = ceil(pikkus / postidevahe)

print(postid)
