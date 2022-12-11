number = int(input('Sisestage naturaalarv:'))

square_of_sums = 0
sum_of_squares = 0

for i in range(1, number+1):
    square_of_sums += i
    sum_of_squares += i**2
square_of_sums = square_of_sums**2

print(square_of_sums - sum_of_squares)