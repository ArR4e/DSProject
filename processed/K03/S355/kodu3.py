n = int(input("Sisesta naturaalarv:"))
nS = (n*(n+1)/2)**2
nV = (n*(n+1)*(2*n+1)/6)
print(int(nS - nV))