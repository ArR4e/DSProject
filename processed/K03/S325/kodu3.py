n= int(input("sisesta naturaalarv n:"))
rs = 0
sr = 0
s = 0
i = 1
while i <= n:
    rs += i**2
    s += i
    i +=1
sr = s**2
vahe = abs(sr-rs)
print(vahe)