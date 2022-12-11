def võitja(maatriks):
    loendurid={'O':0,'X':0}
    for sümbol in 'XO':
        for rida in range(len(maatriks)):
            for veerg in range(len(maatriks[rida])):
                if  veerg < len(maatriks[rida])-2:
                    if (maatriks[rida][veerg]+maatriks[rida][veerg+1]+maatriks[rida][veerg+2]).replace(" ", "") == sümbol*3:
                        loendurid[sümbol] += 1
                if rida < len(maatriks)-2:
                    if (maatriks[rida][veerg]+maatriks[rida+1][veerg]+maatriks[rida+2][veerg]).replace(" ", "") == sümbol*3:
                        loendurid[sümbol] += 1
                if rida < len(maatriks)-2 and veerg < len(maatriks[rida])-2:
                    if (maatriks[rida][veerg]+maatriks[rida+1][veerg+1]+maatriks[rida+2][veerg+2]).replace(" ", "") == sümbol*3:
                            loendurid[sümbol] += 1
                if rida < len(maatriks)-2 and veerg > 1:
                    if (maatriks[rida][veerg]+maatriks[rida+1][veerg-1]+maatriks[rida+2][veerg-2]).replace(" ", "") == sümbol*3:
                        loendurid[sümbol] += 1
    return loendurid



print(võitja([['O',' ','O','X'],
              ['O','O','X','X'],
              ['O','X','O',' '],
              ['X','X','X','O']]))