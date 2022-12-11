fail=input('sisesta failinimi: ')
bussid=[]
sobivad=[]
with open (fail) as file:
    for rida in file:
        rida=rida.split()
        bussid.append(rida)
        #vljub saabub hind
#print(bussid)
for buss in bussid:
    sobib=True
    for buss2 in bussid:
        if buss[0]<buss2[0] and buss[1]>buss2[1] and float(buss[2])>float(buss2[2]):
            sobib=False
    if sobib==True:
        sobivad.append(buss)
sobivad.sort()
print('mõistlikud bussid on:')
for bus in sobivad:
    print(bus[0],bus[1],bus[2])
        