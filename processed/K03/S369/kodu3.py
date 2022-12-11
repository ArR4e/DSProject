n = int(input("Sisesta naturaalarv: "))

def ruutude_summa():
    i = 0
    s = 0
    while i <= n:
        s += i**2
        i += 1
    return(s)
    
#ruutude_summa()

def summa_ruut():
    x = 0
    y = 0
    while x < n:
        x += 1
        y += x
    return (y**2)
    
def erinevus():
    e = summa_ruut() - ruutude_summa()
    print(e)
    
erinevus()



