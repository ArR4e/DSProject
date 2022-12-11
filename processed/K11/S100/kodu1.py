def seosta_lapsed_ja_vanemad(a, b):
    lapsfail = open(a, 'r', encoding = 'UTF-8')
    nimifail = open(b, 'r', encoding = 'UTF-8')
    
    dic = {}
    
    arr = []
    
    for i in nimifail:
        temp = i.split(' ', 1)
        arr.append(temp[0])
        arr.append(temp[1].rstrip())
    
    nimifail.close()
    
    for i in lapsfail:
        temp = i.split(' ')
        if arr[arr.index(temp[1].strip())+1] not in dic.keys():
            dic[arr[arr.index(temp[1].strip())+1]] = []
        dic[arr[arr.index(temp[1].strip())+1]].append(arr[arr.index(temp[0])+1])
    
    lapsfail.close()
    
    for i in dic:
        dic[i] = set(dic[i])
    
    return dic


sonastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for i in sonastik:
    #print(f'{i}: {sonastik[i][0] + ", " + sonastik[i][1] if len(sonastik[i]) != 1 else sonastik[i][0]}')
    print(f'{i}: {sonastik[i].pop()}{", " + sonastik[i].pop() if len(sonastik[i]) != 0 else ""}')