fail = open("kinganumbrid.txt", 'r')
while True:
    try:
        number = fail.readline()
        if number == '':
            break
        number = float(number)
        if number <= 0:
            raise Exception
        print(round(2 / 3 * (number - 2)))
    except:
        print("Vigane sisend")