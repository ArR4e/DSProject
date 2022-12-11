x = open('kinganumbrid.txt')
for sisu in x:
    try:
        print(round(2/3 * (float(sisu) - 2)))
    except:
        print('Vigane sisend!')
x.close()