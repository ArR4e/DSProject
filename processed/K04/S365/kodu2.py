u= float(input("Esimese objekti kiirus: "))
v= float(input("Teise objekti kiirus: "))
x= float(input("Kolmanda objekti kiirus: "))
y= float(input("neljanda objekti kiirus: "))
c= float(299792.458)

def summa(m,n):
    return ((m+n)/(1+((m*n)/(c**2))))

uv=summa(u,v)
uvx=summa(uv,x)
print(summa(uvx,y))

