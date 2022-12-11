x = float(input( " Sisesta aastatulu: "))
if x <= 6000 :
    print( " Maksuvaba tulu on " , x , " eurot ")
elif x > 6000 and x <= 14400:
    print( " Maksuvaba tulu on 6000 eurot " )
elif (x > 14400 and x <= 25200):
    y = (6000 - 6000/10800*(x-14400))
    z = round (y, 2)
    print( " Maksuvaba tulu on " , z , " eurot " )
if (x > 25200):
    print( " Maksuvaba tulu on 0 eurot " )