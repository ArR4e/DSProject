def moos(large_jars, small_jars, jam_amount):
    if large_jars * 5 + small_jars < jam_amount: return -1
    if jam_amount == 0: return 0
    
    jars = 0
    for jar in range(large_jars):
        if jam_amount < 5: break
        jam_amount -= 5
        jars += 1
        if jam_amount == 0: return jars
        
    for jar in range(small_jars):
        jam_amount -= 1
        jars += 1
        if jam_amount == 0: return jars
        
    return -1
