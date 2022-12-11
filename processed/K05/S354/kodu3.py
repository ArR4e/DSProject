def moos(a, b, c): #a=5, b=1
    if c % 5 <= b:
        if a * 5 >= c:
           b_1 = c % 5
           a_1 = (c - b_1) // 5
           if a_1 <= a: 
               return(int(a_1 + b_1))
           if a_1 > a:
                return(str(-1))
        if (a * 5) < c:
            b_1 = c - (a * 5)
            
            if b_1 <= b:
                 
                return(int(a + b_1))
            else:
                return(str(-1))
    else:
        return(str(-1))
