n = int(input("Sisesta naturaalarv "))
x = 1
summ_r=0
r_summ=0
while x!=n+1:
    summ_r+=x
    r_summ+=x**2
    x+=1

summ_r=summ_r**2
print(summ_r - r_summ)