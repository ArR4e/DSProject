def rek_abs(järjend):
    if järjend==[]:
        return []
    else:
        muudetud=[]
        for i in range(len(järjend)):
            if isinstance(järjend[i], list):
                muudetud.append(rek_abs(järjend[i]))
            else:
                muudetud.append(abs(järjend[i]))
        return muudetud
            
                
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))        
        
    