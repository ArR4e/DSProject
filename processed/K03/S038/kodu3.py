n=int(input("Sisestage naturaalarvude kogus:"))
sum=((n/2)*(2+(n-1)))**2
sq=0
for s in range(1,n+1):
    sq=sq+(s**2)
print(int(sum-sq))