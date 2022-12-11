def digonaalid(T,lst):
    arv = 0
    if lst[0][0]== T and lst[1][1] == T or lst[3][3]== T and lst[2][2] == T:
        if lst[0][0]== T and lst[1][1] == T and lst[2][2] == T or lst[1][1] == T and lst[2][2] == T and lst[3][3] == T :
            if lst[0][0]== T and lst[1][1] == T and lst[3][3]== T and lst[2][2] == T:
                arv +=2
            else:
                arv +=1
        else:
            arv +=1
    elif lst[0][3]== T and lst[1][2] == T or lst[3][0]== T and lst[2][1] == T :
        
        if lst[0][3]== T and lst[1][2] == T and lst[2][1] == T or lst[1][2] == T and lst[2][1] == T and lst[3][0] == T :
            if lst[0][3]== T and lst[1][2] == T and lst[3][0]== T and lst[2][1] == T:
                arv +=2
            else:
                arv +=1
        else:
            arv +=1
    return arv
def veerg(T,lst,järk):
    arv = 0
    if lst[0][järk]== T and lst[1][järk] == T or lst[3][järk]== T and lst[2][järk] == T:
        if lst[0][järk]== T and lst[1][järk] == T and lst[2][järk] == T or lst[1][järk] == T and lst[2][järk] == T and lst[3][järk] == T :
            if lst[0][järk]== T and lst[1][järk] == T and lst[3][järk]== T and lst[2][järk] == T:
                arv +=2
            else:
                arv +=1
        else:
            if lst[1][järk]== " " and lst[2][järk]== " ":
                arv +=0
            else:
                arv +=1
    return arv       
def rida(T,lst,järk):
    arv = 0
    if lst[järk][0]== T and lst[järk][1] == T or lst[järk][2]== T and lst[järk][3] == T:
        if lst[järk][0]== T and lst[järk][1] == T and lst[järk][2] == T or lst[järk][1] == T and lst[järk][2] == T and lst[järk][3] == T :
            if lst[järk][0]== T and lst[järk][1] == T and lst[järk][2]== T and lst[järk][3] == T:
                arv +=2
            else:
                arv +=1
        else:
            if lst[järk][1]== " " and lst[järk][2]== " ":
                arv +=0
            else:
                arv +=1
    return arv            
def kontoll(T,lst):
    arv = 0
    lisad = [0,2]
    for i in lisad:
        if lst[(0+i)][0]== T and lst[(1+i)][0]== T and lst[(1+i)][1]== T or lst[(0+i)][0]== T and lst[(0+i)][1]== T and lst[(1+i)][1]== T or lst[(0+i)][1]== T and lst[(1+i)][0]== T and lst[(1+i)][1]== T:
            if lst[(0+i)][0]== T and lst[(1+i)][0]== T and lst[(1+i)][1]== T and lst[(0+i)][1] == T:
                arv -= 2
            else:
               arv -= 1
    for i in lisad:
        if lst[0][(0+i)]== T and lst[1][(0+i)]== T and lst[1][(1+i)]== T or lst[0][(0+i)]== T and lst[0][(1+i)]== T and lst[1][(1+i)]== T or lst[0][(1+i)]== T and lst[1][(0+i)]== T and lst[1][(1+i)]== T:
            if lst[0][(0+i)]== T and lst[1][(0+i)]== T and lst[1][(1+i)]== T and lst[0][(1+i)] == T:
                arv -= 2
            else:
               arv -= 1
    print(T,arv)
    return arv
def kõiik_või_ei_midagi(T,lst,T_vastand):
    sõna = ""
    for i in lst:
        for j in i:
           sõna += j 
    if T_vastand in sõna or " " in sõna:
        return 0
    else:
        return 1

def võitja(lst):
    d = {"O":0,"X":0}
    #diagonaalid
    d["O"] += digonaalid("O",lst)
    d["X"] += digonaalid("X",lst)
    #veerg ja rida
    for i in range(4):
        d["O"] += veerg("O",lst,i)
        d["X"] += veerg("X",lst,i)
        d["O"] += rida("O",lst,i)
        d["X"] += rida("X",lst,i)
        
    #kontroll et midagi ei oleks toppelt
    #d["O"] += kontoll("O",lst)
    #d["X"] += kontoll("X",lst)
    
    sisu1 = kõiik_või_ei_midagi("O",lst,"X")
    sisu2 = kõiik_või_ei_midagi("X",lst,"O")
    if sisu1 == 1:
        d["O"] = 24
        d["X"] = 0
    elif sisu2 == 1:
       d["X"] = 24
       d["O"] = 0
    
    return d
            
    
    
    
    

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))

