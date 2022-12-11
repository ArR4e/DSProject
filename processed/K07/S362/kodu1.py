def poisse_ja_tüdrukuid(järjend):
    m=0
    n=0
    for el in järjend:
        a=el.split(" ")
        c=len(a)
        if c>2:
            b=a[2]
            if b=="P":
#                 print("On poiss")
                m=m+1
            
            elif b=="T":
#                 print("On tüdruk")
                n=n+1
        elif c==2:
             b=a[1]
             if b=="P":
#                  print("On poiss")
                 m=m+1
            
             elif b=="T":
#                  print("On tüdruk")
                 n=n+1
    
    return (m,n)
    
# 'Mati P', 'Siim Aleksander P',  'Jüri P',  
järjend=['Mati P', 'Siim Aleksander P',  'Jüri P', 'Kati T', 'Veronika T']
# 'Kati T', 'Veronika T'
(poiste_arv,tüdrukute_arv)=poisse_ja_tüdrukuid(järjend)
# 
print("("+str(poiste_arv)+","+str(tüdrukute_arv)+")")