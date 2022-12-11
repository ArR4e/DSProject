arv = int(input("Sisesta naturaalarv: "))

squareSum = 0
cubeSum = 0

for i in range(1, arv+1):
    squareSum += i**2

for i in range(1, arv+1):
    cubeSum += i

cubeSumSquared = cubeSum**2

print(cubeSumSquared-squareSum)