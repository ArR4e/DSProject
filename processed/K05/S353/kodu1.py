user=input('Palun sisestage oma kasutajanimi: ')
while True: 
    par1=input('Palun sisestage oma parool: ')
    par2=input('Palun sisestage oma parool uuesti: ')
    if par1 != par2:
        print('Paroolid ei ole samad!')
        continue
    elif len(par1)<8:
        print('Parool peab olema vähemalt 8 tähemärki pikk!')
        continue
    i=0
    x=0
    y=0
    while i<len(par1):
        täht= par1[i]
        if täht.isalpha():
            y+=1
        elif täht.isnumeric():
            x+=1
        i+=1
    if x==0:
        print('Parool peab sisaldama numbrit!')
        continue
    if y==0:
        print('Parool peab sisaldama tähti!')
        continue
    break
def tagurpidi(sona):
    i1=0
    tagurpidisona=''
    while i1<len(sona):
        tagurpidisona+=sona[len(sona)-i1-1]
        i1+=1
    return tagurpidisona
tagurpidiparool=tagurpidi(par1)
fail=open('users.txt', 'w')
fail.write(user+':'+tagurpidiparool)
fail.close()