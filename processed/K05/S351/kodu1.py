#Viimased kaks käsku ilma tsükklita
def pooramine_ja_kirjutamine(kasutajanimi, parool1):
    parooli_pikkus=len(parool1)
    pooratud_parool=parool1[parooli_pikkus::-1]
    fail=open("users.txt", "w")
    fail.write(str(kasutajanimi)+":"+ str(pooratud_parool))
 
#paroolis numbrid ja tähed
def kas_on_numbrid_ja_tahed(parool1):
    number=1
    taht=1
    for element in parool1:
        if element.isdigit():
            number=2
        elif element.isalpha():
                taht=2
    if number==2 and taht==2:
            return (True)
    else:
            return (False)
            
       
#kasutajanime küsimine väljaspool tsükklit
kasutajanimi=input("Sisestage kasutajanimi: ")

#tsükkel

while True:
    parool1=input("Sisestage esimene parool: ")
    parool2=input("Sisestage teine parool: ")
    tahti_paroolis=len(parool1)
    if parool1!=parool2:
        print("Esimene parool ei ole vastavuses teise parooliga")
    elif tahti_paroolis<8:
        print("Paroolis ei ole kaheksat tähemärki")
    elif not kas_on_numbrid_ja_tahed(parool1):
        print("Paroolis ei ole nii numbreid kui ka tähti")
    else:
        break
    

pooramine_ja_kirjutamine(kasutajanimi, parool1)
print("Teie kasutajanimi ja parool on edukalt faili kirjutatud")
                
            

            
        
        