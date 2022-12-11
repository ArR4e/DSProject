def väljasta_liin(eel,järg,d,alg=0,x=0):
    if x==0:
        alg=järg
    if järg in d:
        if eel in d[järg]:
            print(eel)
            if x==0:
                        väljasta_liin(0,0,d,alg,-1)
            return True
        else:
            for i in range(2):
                y=väljasta_liin(eel,d[järg][i],d,alg,x+1)
                if y== True:
                    print(d[järg][i])
                    if x==0:
                        väljasta_liin(0,0,d,alg,-1)
                    return True
        return False
    elif x==-1:
        print(alg)
    else:
        return False

    
d={  'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'),'Rita': ('Teet', 'Maris'),'Siim': ('Teet', 'Maris'),'Mari': ('Karl', 'Leeni'),'Teet': ('Joosep', 'Adele'),'Adele': ('Johannes', 'Leida'),'Konstantin': ('Viktor', 'Jelena'),'Joosep': ('August', 'Emma'),'Viktor': ('Nikolai', 'Maria')}

print("Kas liin leidub?",väljasta_liin("Leida","Kalle",d))
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele',d))