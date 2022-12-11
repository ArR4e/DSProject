a=int(input("Naturaalarv: "))
sr=((a/2)*(2+(a-1)))**2
rs=0
for r in range(1,a+1):
    rs=rs+(r**2)
print(int(sr-rs))