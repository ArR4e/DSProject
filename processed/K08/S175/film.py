
def loetleFilmid(zanri_nimi):
    f = open("filmid.txt", encoding = 'utf-8')
    filmi_nimed = f.readlines()
    if zanri_nimi in filmi_nimed:
         filmi_nimed = [filmi_nimed.strip-zanri_nimi]
         return  filmi_nimed
    f.close()
   
   
      

   
   
    
    
    

    