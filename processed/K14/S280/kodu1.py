def rek_abs(järjend):
    
    uus = []
        
    for i,el in enumerate(järjend):
        if isinstance(el, list) == True:
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
              
    print(järjend)
    return uus

print(rek_abs([-5, -6, [-1,-2,[-3]], -7]))