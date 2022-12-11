def moos(karp1, karp2, kg):
    karpe= karp1 +karp2
    while True:
        if kg>=5 and karp1>0:
            karp1 -=1
            kg= kg-5
        elif kg <= karp2:
            karp2 -=1
            kg = kg-1
        else:
             return -1
        if kg == 0:
            vastus = karpe-(karp1 + karp2)
            return vastus
        
   

         
