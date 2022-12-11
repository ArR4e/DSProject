

def rek_abs(jrj):
    
    if isinstance(jrj, list)==False:
            return abs(jrj)
        
    koopia=jrj.copy()
    
    for i in range(len(koopia)):

            koopia[i]=rek_abs(koopia[i])
        
    return koopia
    
jrj1=   [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
print(rek_abs(jrj1))
