from math import ceil

line_length = int(input('Sisestage liini pikkus: '))
post_distance = int(input('Sisestage kahe posti vaheline kaugus: '))

post_amount = ceil(line_length / post_distance) + 1
print(f'Liini ehitamiseks on vaja minimaalselt {post_amount}')