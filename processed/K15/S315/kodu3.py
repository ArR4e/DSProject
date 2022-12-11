
fail = str(input("fail! "))

bussid = []
sobivad_bussid = []

with open (fail, 'r', encoding = 'utf-8') as f:
    for rida in f:
        info = rida.strip().split(' ')
        bussid.append(info)  
        
for buss in range(len(bussid)):
    sobib = True
    for buss2 in range(buss+1, len(bussid)):
        if bussid[buss][0] < bussid[buss2][0] and bussid[buss][1] > bussid[buss2][1] and bussid[buss][2] > bussid[buss2][2]:
            sobib = False
        if sobib == True:
            sobivad_bussid.append(bussid[buss])
        
        
print(sobivad_bussid)
        