import re

bussid = []
with open("sõiduplaan.txt") as f:
    for i in f.readlines():
        bussid.append([int(re.findall("[0-9]{1}$", i)[0]), [int(x) for x in re.findall("[0-5][0-9]", i)]])

halvadbussid = []

for buss in bussid:
    for buss2 in bussid:
        if buss2 != buss:
            if buss[0] > buss2[0] and buss[1][0] < buss2[1][0] or buss[1][0] > buss2[1][0] and buss[1][1] < buss2[1][1] and buss[1][2] < buss2[1][2] or buss[1][2] > buss2[1][2] and buss[1][3] < buss2[1][3]:
                halvadbussid.append(buss)
                
for buss in bussid:
    if buss not in halvadbussid:
        print(f"{buss[1][0]}:{buss[1][1]} {buss[1][2]}:{buss[1][3]} {buss[0]}")
