
def rek_abs(x):
    m=[]
    if isinstance(x, list):
        for i in range (len(x)):
            try:
                if x[i]<0:
                    m.append(-x[i])
                else:
                    m.append(x[i])
            except:
                
                m.append(rek_abs(x[i]))
        
    return m
            
    


print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))