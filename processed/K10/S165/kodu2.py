def võitja(maatriks):
    
    O_võidud = 0
    X_võidud = 0
    
    #horisontaal
    for el in maatriks:
        el = "".join(el)
        if el == "OOOO":
            O_võidud += 2
        elif el == "OOOX" or el == "OOO " or el == "XOOO" or el == " OOO":
            O_võidud += 1
        elif el == "XXXX":
            X_võidud += 2
        elif el == "XXXO" or el == "XXX " or el == "OXXX" or el == " XXX":
            X_võidud += 1
            
     #vertikaal
    
    for i in range(0,4):
         ls = []
         for el in maatriks:
             ls.append(el[i])
         sõne = "".join(ls)
         if sõne == "OOOO":
             O_võidud += 2
         elif sõne == "OOOX" or sõne == "OOO " or sõne == "XOOO" or sõne == " OOO":
            O_võidud += 1
         elif sõne == "XXXX":
             X_võidud += 2
         elif sõne == "XXXO" or sõne == "XXX " or sõne == "OXXX" or sõne == " XXX":
             X_võidud += 1
    
    
    #diagonaal
    peadiagonaal1 = ""
    peadiagonaal2 = ""
    diagonaal1 = ""
    diagonaal2 = ""
    diagonaal3 = ""
    diagonaal4 = ""
    
    
    
    for i in range(0,4):
       peadiagonaal1 += maatriks[i][i]
       peadiagonaal2 += maatriks[i][-(i+1)]
       
       
       if i < 3:
           diagonaal1 += maatriks[i][i+1]
           diagonaal2 += maatriks[i+1][i]
          
           diagonaal3 += maatriks[i][-(i+2)]
           diagonaal4 += maatriks[i+1][-(i+1)]
    
    diagonaalide_list = [peadiagonaal1, peadiagonaal2, diagonaal1,
                         diagonaal2, diagonaal3, diagonaal4]
    for sõne in diagonaalide_list:
        if sõne == "OOOO":
             O_võidud += 2
        elif sõne == "OOOX" or sõne == "OOO " or sõne == "XOOO" or sõne == " OOO" or sõne == "OOO":
            O_võidud += 1
        elif sõne == "XXXX":
             X_võidud += 2
        elif sõne == "XXXO" or sõne == "XXX " or sõne == "OXXX" or sõne == " XXX" or sõne == "XXX":
             X_võidud += 1
        
    return { "O": O_võidud, "X": X_võidud }       
        
        
        
            





    
        
        
    
    











