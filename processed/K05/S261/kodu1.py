nimi=input('Sisesta kasutajanimi:')

num=taht=False

while (num==False)or(taht==False):
    num=taht=False
    
    a=input('Sisesta parool:')
    b=input('Sisesta parool uuesti:')
    
    x=list(a)

    if a==b:
        if len(a)>=8:
            for i in range(len(a)):
                if str(x[i]).isdigit():
                    num=True
                else:
                    taht=True
            if (taht==False)or(num==False):
                print('Parool peab sisaldama numbreid ja tähti!')
            else:
                break
                    
        else:
            print('Parool on liiga lühike!')
    else:
        print('Sisestasid erinevad paroolid!')
        
c=a[::-1]

f=open('users.txt','w')

f.write(nimi+':'+c)

f.close()
