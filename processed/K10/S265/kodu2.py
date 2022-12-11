def võitja(matrix):
    result = {'O': 0, 'X': 0}
    for countrows, row in enumerate(matrix):
        for countcolumns, column in enumerate(matrix):
            try:
                if matrix[countrows][countcolumns] == 'X' and matrix[countrows][countcolumns-1] == 'X' and matrix[countrows][countcolumns+1] == 'X':
                    result['X'] += 1
                    print('x horizontal at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'X' and matrix[countrows-1][countcolumns] == 'X' and matrix[countrows+1][countcolumns] == 'X':
                    result['X'] += 1
                    print('x vertical at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'X' and matrix[countrows+1][countcolumns-1] == 'X' and matrix[countrows-1][countcolumns+1] == 'X':
                    result['X'] += 1
                    print('x diagonal rising at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'X' and matrix[countrows+1][countcolumns+1] == 'X' and matrix[countrows-1][countcolumns-1] == 'X':
                    result['X'] += 1
                    print('x diagonal falling at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'O' and matrix[countrows][countcolumns-1] == 'O' and matrix[countrows][countcolumns+1] == 'O':
                    result['O'] += 1
                    print('o horizontal at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'O' and matrix[countrows-1][countcolumns] == 'O' and matrix[countrows+1][countcolumns] == 'O':
                    result['O'] += 1
                    print('o vertical at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'O' and matrix[countrows+1][countcolumns-1] == 'O' and matrix[countrows-1][countcolumns+1] == 'O':
                    result['O'] += 1
                    print('o diagonal rising at ',(countrows, countcolumns))
                if matrix[countrows][countcolumns] == 'O' and matrix[countrows+1][countcolumns+1] == 'O' and matrix[countrows-1][countcolumns-1] == 'O':
                    result['O'] += 1
                    print('o diagonal falling at ',(countrows, countcolumns))
            except:
                pass
    return result