#s = '12.45'
#print(int(s[:-3]) * 60 + int(s[-2:]))
def calculate(line):
    temp = 0
    for n in range(2):
        temp += (int(line[n][:-3]) * 60 + int(line[n][-2:]))
    temp *= int(line[2])
    
    return temp


def console_log(n, indexes):
    with open(n) as f:
        for index, line in enumerate(f):
            if (index in indexes):
                print(line.strip())


def times(n):
    times = []
    indexes = []
    with open(n) as f:
        for line in f.readlines():
            line = line.strip().split(' ')

            times.append(calculate(line))
    for i in range(3):
        index = times.index(min(times)) 

        indexes.append(index)
        times[index] = 100000000000
        
    console_log(n, indexes)
    


times('sõiduplaan.txt')
