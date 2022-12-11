def hinna_arvutamine(kilomeetrid):
    global odavtakso
    takso2 = takso.readline().strip().split(",")
    takso3 = takso.readline().strip().split(",")
    
    takso1hind = float(takso1[1]) + float(takso1[2])*kilomeetrid 
    takso2hind = float(takso2[1]) + float(takso2[2])*kilomeetrid 
    takso3hind = float(takso3[1]) + float(takso3[2])*kilomeetrid
    
    taksohinnad = [takso1hind, takso2hind, takso3hind]
    parimval = min(taksohinnad)
    odavindeks = taksohinnad.index(parimval)
    odavtakso = "" 
    if odavindeks == 0:
        odavtakso = takso1[0]
    elif odavindeks ==1:
        odavtakso = takso2[0]
    else:
        odavtakso = takso3[0]
    return odavtakso


takso = open("taksohinnad.txt")
kilomeetrid = float(input("Sisesta reisitavad kilomeetrid: "))
takso1 = takso.readline().strip().split(",")
if takso1 != ['']:
    hinna_arvutamine(kilomeetrid)
    print("Kõige odavam takso on " + odavtakso)
else:
    print("Täna pead kahjuks koju jalutama!")
    
takso.close()