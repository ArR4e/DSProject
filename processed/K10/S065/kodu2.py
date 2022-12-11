# Ülesanne 2

def võitudearv(a, sümbol):
    
    kokku = 0
    
    for i in range(len(a)):
        for l in range(len(a[i])-2):
            if a[i][l] ==a[i][l+1] ==a[i][l+2] == sümbol:
                kokku += 1
    
    for i in range(len(a)-2):
        for l in range(len(a[i])):
            if a[i][l] == a[i+1][l] == sümbol:
                kokku += 1
                
    for i in range(len(a)-2):
        for l in range(len(a[i])-2):
            if a[i][l] == a[i+1][l+1] == a[i+2]== sümbol:
                kokku += 1
    
    for i in range(len(a)-2):
        for l in range(2, len(a[i])):
            if a[i][l] == a[i+1][l-1] == a[i+2][l-2] == sümbol:
                kokku += 1
    
    return kokku

def võitja(a):
    võit_O = võitudearv(a, 'O')
    võite_X = võitudearv(a, 'X')
    return {'O': võite_O, 'X': võite_X}