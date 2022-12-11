filename = str(input('sisesta failinimi: '))
print("esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")

def järjesta_punktid(array):
    for y in range(len(array)-1):
        for x in range(len(array)-y-1):
            if array[x][1] > array[x+1][1]:
                array[x], array[x+1] = array[x+1], array[x]
    return array


with open(filename,'r',encoding='utf8') as f:
    array_start = [x.strip() for x in f.readlines()]
    array = [x.split() for x in array_start]
    for x in range(len(array)):
        array[x][0]=int(array[x][0][:2]) + float(int(array[x][0][3:5])/60)
        array[x][1]=int(array[x][1][:2]) + float(int(array[x][1][3:5])/60)
    array_sort = []
    for x in range(len(array)):
        array_sort.append((x,array[x][0]))
järjesta_punktid(array_sort)
array_remove = []
for x in range(len(array)):
    for y in range(len(array)):
        if array[x][0] < array[y][0] and array[x][1] > array[y][1] and int(array[x][2]) > int(array[y][2]):
            array_remove.append(x)

for x in range(0,len(array_start)):
    if array_sort[x][0] not in array_remove:
        print(array_start[array_sort[x][0]])