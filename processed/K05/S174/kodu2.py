from random import randint
def suurväike(sõna):
    töödeldud_sõna = ""
    märgid = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    juhuslik_märk = märgid[randint(0,len(märgid))]
    #hakkan võtma iga sõna karakterit eraldi
    
    for i in range(len(sõna)):
        karakter = sõna[i]
        #kontrollin kas tegemist on tähega
        if karakter.isalpha():
            if karakter.isupper():
                töödeldud_sõna += karakter.lower()
            else:
                töödeldud_sõna += karakter.upper()
        #kontrollin kas tegemist on tühikuga
        elif karakter == " ":
            töödeldud_sõna += " "
        #siin peab olema tegemist märgiga
        else:
            töödeldud_sõna += juhuslik_märk
    
    return töödeldud_sõna
                
    

