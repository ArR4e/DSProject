f = open('kinganumbrid.txt')
output = ''

line = f.readline()
while line != '':
    try:
        output += str(round(2 / 3 * (float(line.strip()) - 2)))
    except:
        output += 'Vigane sisend'
    line = f.readline()
    if line == '':
        break
    output += '\n'

f.close()
print(output)