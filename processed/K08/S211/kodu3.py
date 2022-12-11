import film

def töötleKäsk(tähis, jrj):
    
    if jrj==[]:
        return False
    
    elif tähis == 'K':
        #koostab uue järjendi filmidega sellest žanrist, mis kasutaja sisestas
        filmid = film.loetleFilmid(jrj[0])
        print("Võimalikud filmid on: \n")
        for el in filmid:
            print(el, '\n')
            
        return(True)
        
    elif tähis == 'L':
        
        if len(jrj) >= 2:
            
            pealkiri_jrj = jrj[1:(len(jrj))]
            pealkiri = " ".join(pealkiri_jrj)
            žanr = jrj[0]
            film.lisaFilm(pealkiri, žanr)
            print("Film lisatud!")
            
        else:
            print("Miskit läks nihu :/ Proovi uuesti!")
        return(True)
        
    elif tähis=='V':
        if len(jrj)>1:
            
            pealkiri_jrj = jrj[0:(len(jrj))]
            pealkiri = " ".join(pealkiri_jrj)
            
        else:
            pealkiri = jrj[0]
            
        print(pealkiri)
        film.kustutaFilm(pealkiri)
        print("Head vaatamist! :)")
        return (True)
        
    elif tähis=='E':
        
        return(False)
        

print(" FILMIANDMEBAAS ".center(34, "="),'\n'
      "Kuva filmid:\tK <žanr> \n",
      "Lisa film:\tL <žanr> <film> \n",
      "Vaata filmi:\tV <filmi nimi> \n",
      "Lõpeta:\t\tE \n",
      "***".center(34, "="),
      sep="")

a = True

while a is True:
    
    sisend = input("")

    sisendi_jrj = sisend.split(" ")
    
    käsk = sisendi_jrj[0]
    argumendid = sisendi_jrj[1:(len(sisendi_jrj))]
    
    a = töötleKäsk(käsk, argumendid)
