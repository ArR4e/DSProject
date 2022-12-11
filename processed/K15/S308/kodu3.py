#fail=input('Sisestage failinimi: ')
fail='uus.txt'
f=open(fail)
tühi=[]
for i in f:
    i=i.strip()
    osad=i.split(' ')
    tühi.append(osad)
for i in range (len(tühi)-1):
    if tühi[i][i]< tühi [i+1][i]:
        if tühi[i][i+1]<tühi [i+1][i+1]:
            if tühi[i][-1]<tühi[i+1][-1]:
                print(tühi[i])
print(tühi)
    
#     for j in osad:
#         osad2=j.split(':')
#         try:
#             kell=(osad2[0]+'.'+osad2[-1])
#         print(osad2)
    