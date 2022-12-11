n = int(input("Sisesta arv: "))
print(sum(list(range(n+1))[1:])**2-sum(map(lambda a:a**2,list(range(n+1)[1:]))))