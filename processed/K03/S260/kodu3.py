n = int(input("Sisesta n: "))

sr,rs=0,0

for i in range(n):
    sr=sr+(i+1)**2
    rs=rs+(i+1)
    
print((rs**2)-sr)
