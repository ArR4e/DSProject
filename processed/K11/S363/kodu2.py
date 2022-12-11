def transponeeriK(m):
    t = []
    järjend = []
    for x in range(len(m)):
        järjend.append("-")
    for y in range(len(m[0])):
        t.append(järjend.copy())
            
    for i in range(len(t)):
        for j in range(len(t[i])):
            t[i][j] = m[len(t[i])-j-1][len(t)-i-1]
    
    return t
